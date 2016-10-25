from __future__ import unicode_literals

from jsonapi_mock_server.base_models import BaseResource
from jsonapi_mock_server import fake


class QuestionResource(BaseResource):
    resource_type = 'Question'
    attributes = {
        'question_text': 'What is your favorite book?'
    }
    fake_attributes = {
        fake.StringFaker("words")
    }
