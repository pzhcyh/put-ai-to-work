import json
import unittest

from app import AdapterError, AppError, answer, parse_request


def request(question, **extra):
    return json.dumps({"question": question, **extra}, ensure_ascii=False)


class ExampleTests(unittest.TestCase):
    def assert_code(self, code, function, *args, **kwargs):
        with self.assertRaises(AppError) as caught:
            function(*args, **kwargs)
        self.assertEqual(caught.exception.code, code)

    def test_borrow_quote(self):
        result = answer(request("借阅期限是多少？"))
        self.assertEqual(result["citations"], ["borrow-v1"])
        self.assertIn("14天", result["answer"])
        self.assertEqual(result["mode"], "mock")

    def test_missing_evidence(self):
        result = answer(request("逾期罚款多少钱？"))
        self.assertEqual(result["status"], "insufficient_evidence")
        self.assertEqual(result["citations"], [])

    def test_public_cannot_read_staff(self):
        result = answer(request("管理员值班电话是什么？"))
        self.assertEqual(result["status"], "insufficient_evidence")
        self.assertNotIn("000", result["answer"])

    def test_trusted_staff_can_read(self):
        result = answer(request("管理员值班电话是什么？"), group="staff")
        self.assertEqual(result["citations"], ["desk-v1"])

    def test_cannot_set_group_in_json(self):
        self.assert_code("invalid_request", answer, request("管理员电话", group="staff"))

    def test_invalid_json(self):
        self.assert_code("invalid_json", parse_request, "{broken")

    def test_question_boundaries(self):
        for question in ("", "  ", 12, "借" * 401):
            self.assert_code("invalid_question", parse_request, request(question))

    def test_k_boundaries(self):
        for k in (True, 0, 4, "2", 1.2):
            self.assert_code("invalid_k", parse_request, request("借阅", k=k))

    def test_request_size(self):
        self.assert_code("request_too_large", parse_request, " " * 4097)

    def test_bad_citation_rejected(self):
        class BadAdapter:
            def generate(self, question, documents):
                return {"status": "answered", "answer": "伪造引用", "citations": ["not-found"], "mode": "mock"}
        self.assert_code("invalid_citations", answer, request("借阅"), adapter=BadAdapter())

    def test_malformed_output_rejected(self):
        class BadAdapter:
            def generate(self, question, documents):
                return "not an object"
        self.assert_code("invalid_output", answer, request("借阅"), adapter=BadAdapter())

    def test_adapter_unavailable(self):
        class FailedAdapter:
            def generate(self, question, documents):
                raise AdapterError("simulated failure")
        self.assert_code("service_unavailable", answer, request("借阅"), adapter=FailedAdapter())

    def test_ranking_is_stable(self):
        result = answer(request("借阅期限和开放时间", k=1))
        self.assertEqual(result["citations"], ["borrow-v1"])


if __name__ == "__main__":
    unittest.main()
