from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from resources import choice, question


router = SimpleRouter(trailing_slash=False)
router.register(r'questions', question.QuestionViewSet, base_name='question')
router.register(r'choices', choice.ChoiceViewSet, base_name='choice')
urlpatterns = router.urls
