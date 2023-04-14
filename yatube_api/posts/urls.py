from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', obtain_auth_token),
]
