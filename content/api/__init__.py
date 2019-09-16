from .content import ContentViewSet
from .user import UserCreateViewSet
from contrib.router import HybridRouter


ContentRouter = HybridRouter()
ContentRouter.register('content', ContentViewSet)
ContentRouter.register('user', UserCreateViewSet)
