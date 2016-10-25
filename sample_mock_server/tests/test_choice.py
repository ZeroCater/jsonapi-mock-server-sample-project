from django.core.urlresolvers import reverse

from jsonapi_mock_server import base_tests


class ChoiceTests(base_tests.TestJsonResponses):
    def test_choice_list(self):
        self.path = reverse("choice-list")
        self.do_test()

    def test_choice_detail(self):
        self.path = reverse("choice-detail", args=(1,))
        self.do_test()


class ChoiceFakerTests(base_tests.TestFaker):
    def test_choice_detail(self):
        self.path = reverse("choice-detail", args=(1,))
        self.do_test()
