from __future__ import unicode_literals

from jsonapi_mock_server.base_models import BaseResource
from jsonapi_mock_server.base_views import ResourceViewSet
from jsonapi_mock_server import fake


class ChoiceResource(BaseResource):
    resource_type = 'Choice'
    attributes = {
        'choice_text': 'Moby Dick',
        'votes': 3,
    }
    relationships = [
        ('question', 1)
    ]
    fake_attributes = {
        'choice_text': fake.StringFaker("word"),
        'votes': fake.IntFaker(1,10),
    }


class ChoiceViewSet(ChoiceResource, ResourceViewSet):
    pass
