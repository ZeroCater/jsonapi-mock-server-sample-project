from django.core.urlresolvers import reverse

from jsonapi_mock_server import base_tests


class QuestionTests(base_tests.TestJsonResponses):
    def test_question_list(self):
        self.path = reverse("question-list")
        self.do_test()

    def test_question_detail(self):
        self.path = reverse("question-detail", args=(1,))
        self.do_test()


class QuestionFakerTests(base_tests.TestFaker):
    def test_question_detail(self):
        self.path = reverse("question-detail", args=(1,))
        self.do_test()
