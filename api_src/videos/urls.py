from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateVideoAPIView.as_view(), name='get_post_videos'),
    path('<int:pk>', views.RetrieveUpdateDestroyVideoAPIView.as_view(), name='get_delete_update_video'),
]