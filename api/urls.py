from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupList, CommentViewSet, FollowList
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments',
                CommentViewSet, basename='comments')
router.register(r'group', GroupList, basename='group')
router.register(r'follow', FollowList, basename='follow')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router.urls)),
]
