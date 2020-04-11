from rest_framework import routers
from .views import RegisterAPIView,UserLoginAPIView
from django.contrib import admin
from django.urls import path,include


router=routers.DefaultRouter()
#router.register('api/register',RegisterViewSet,"register")


#urlpatterns = router.urls




urlpatterns = [
    path('api/login/',UserLoginAPIView.as_view()),
    path('api/register/',RegisterAPIView.as_view()),

]

urlpatterns += router.urls
