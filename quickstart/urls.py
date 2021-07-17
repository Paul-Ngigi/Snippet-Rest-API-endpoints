from django.urls import path
from .views import AllPosts, SinglePost


urlpatterns = [
    path('', AllPosts.as_view()),
    path('<int:pk>', SinglePost.as_view()),
]
