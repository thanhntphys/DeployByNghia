from django.conf.urls import url
from django.urls import path,include
from tutorials.views import TutorialRetrieveUpdateDestroyAPIView, tutorial_list_published,TutorialListAPIView

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'api/tutorials', TutorialListViewSet, basename="lis-tutorial")
urlpatterns = [
    #path('api/tutorials', TutorialListAPIView.as_view(), name="tutorial-list"),
    path('api/tutorials/', TutorialListAPIView.as_view(), name="tutorial-list"),
    path('api/tutorials/<int:pk>', TutorialRetrieveUpdateDestroyAPIView.as_view(), name="tutorial-retrive-update-destroy"),
    path('api/tutorials/published', tutorial_list_published),
#     path('', include(router.urls)),
]
