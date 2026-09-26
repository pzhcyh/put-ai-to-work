"""Offline teaching example. No model, network, credentials, or production server."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Protocol


class AppError(Exception):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


class AdapterError(Exception):
    pass


@dataclass(frozen=True)
class Document:
    id: str
    text: str
    version: str
    groups: frozenset[str]
    keywords: tuple[str, ...]


CORPUS = (
    Document("borrow-v1", "借阅期限为14天；到期前可申请一次续借，续借7天。", "2026-09-demo", frozenset({"public", "staff"}), ("借阅", "期限", "续借")),
    Document("hours-v1", "图书角开放时间为周一至周五12:00—18:00。", "2026-09-demo", frozenset({"public", "staff"}), ("开放", "几点", "时间")),
    Document("desk-v1", "模拟管理员值班分机为000，仅供本地教学。", "2026-09-demo", frozenset({"staff"}), ("管理员", "值班", "电话", "分机")),
)


def parse_request(raw: str) -> dict:
    if len(raw.encode("utf-8")) > 4096:
        raise AppError("request_too_large")
    try:
        data = json.loads(raw)
    except (ValueError, RecursionError):
        raise AppError("invalid_json") from None
    if not isinstance(data, dict) or set(data) - {"question", "k"}:
        raise AppError("invalid_request")
    question = data.get("question")
    if not isinstance(question, str) or not 1 <= len(question.strip()) <= 400:
        raise AppError("invalid_question")
    k = data.get("k", 2)
    if type(k) is not int or not 1 <= k <= 3:
        raise AppError("invalid_k")
    return {"question": question.strip(), "k": k}


def retrieve(question: str, k: int, group: str, corpus=CORPUS) -> list[Document]:
    scored = []
    for doc in corpus:
        if group not in doc.groups:
            continue
        score = sum(word in question for word in doc.keywords)
        if score:
            scored.append((score, doc))
    scored.sort(key=lambda item: (-item[0], item[1].id))
    return [doc for _, doc in scored[:k]]


class Adapter(Protocol):
    def generate(self, question: str, documents: list[Document]) -> dict: ...


class MockAdapter:
    """Deterministic quote assembler. This does not call or evaluate a model."""
    def generate(self, question: str, documents: list[Document]) -> dict:
        return {
            "status": "answered",
            "answer": "\n".join(doc.text for doc in documents),
            "citations": [doc.id for doc in documents],
            "mode": "mock",
        }


def validate_response(result, documents: list[Document]) -> dict:
    if not isinstance(result, dict) or set(result) != {"status", "answer", "citations", "mode"}:
        raise AppError("invalid_output")
    if result["status"] != "answered" or result["mode"] != "mock":
        raise AppError("invalid_output")
    answer, citations = result["answer"], result["citations"]
    if not isinstance(answer, str) or not 1 <= len(answer.strip()) <= 2000:
        raise AppError("invalid_output")
    if not isinstance(citations, list) or not citations or any(not isinstance(c, str) for c in citations):
        raise AppError("invalid_output")
    if len(citations) != len(set(citations)) or not set(citations) <= {doc.id for doc in documents}:
        raise AppError("invalid_citations")
    return result


def answer(raw: str, *, group: str = "public", adapter: Adapter | None = None) -> dict:
    """group must come from a trusted caller; never from request JSON."""
    request = parse_request(raw)
    documents = retrieve(request["question"], request["k"], group)
    if not documents:
        return {"status": "insufficient_evidence", "answer": "当前可访问资料中没有找到匹配内容。请换一种问法，或请资料负责人补充。", "citations": [], "mode": "mock"}
    try:
        result = (adapter if adapter is not None else MockAdapter()).generate(request["question"], documents)
    except AdapterError:
        raise AppError("service_unavailable") from None
    return validate_response(result, documents)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", default="借阅期限是多少？")
    args = parser.parse_args()
    try:
        result = answer(json.dumps({"question": args.question}, ensure_ascii=False))
    except AppError as exc:
        print(json.dumps({"status": "error", "code": exc.code, "mode": "mock"}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
