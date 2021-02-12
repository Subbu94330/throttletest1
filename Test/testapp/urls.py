from rest_framework import routers
from .views import PeriodViewSet,UserViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register("periods", views.PeriodViewSet, basename="periods"),
router.register("users", views.UserViewSet, basename="users")

urlpatterns =[

]

urlpatterns += router.urls