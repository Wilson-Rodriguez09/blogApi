from rest_framework.routers import DefaultRouter
from apps.post.api.views import PostViewSet

router_post = DefaultRouter()
router_post.register(prefix="post", basename="post", viewset=PostViewSet) 