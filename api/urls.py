from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>[0-9]+)/comments', CommentViewSet, basename='comments')
router.register('group', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='Follow')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
