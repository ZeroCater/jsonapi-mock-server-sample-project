from jsonapi_mock_server.base_views import ResourceViewSet


from resources.question import QuestionResource
from resources.choice import ChoiceResource


class QuestionViewSet(QuestionResource, ResourceViewSet):
    pass


class ChoiceViewSet(ChoiceResource, ResourceViewSet):
    pass
