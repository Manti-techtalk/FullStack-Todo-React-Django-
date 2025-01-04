from django.urls import path,include
from . import views
from rest_framework import routers
from api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks',views.TaskViewSet)

urlpatterns = [
    path('',views.apiSite),
    path('',include(router.urls)), 
]