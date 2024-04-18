from django.urls import path, include
from .views import PostViewSet, add_comment_to_post
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/comments/', add_comment_to_post, name='add_comment_to_post'),
]