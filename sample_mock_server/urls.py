from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from sample_mock_server import views


router = SimpleRouter(trailing_slash=False)
router.register(r'questions', views.QuestionViewSet, base_name='question')
router.register(r'choices', views.ChoiceViewSet, base_name='choice')
urlpatterns = router.urls
