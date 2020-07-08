from .content import ContentViewSet
from .user import UserCreateViewSet
from .organizacao import OrganizacaoViewSet
from contrib.router import HybridRouter


ContentRouter = HybridRouter()
ContentRouter.register('content', ContentViewSet)
ContentRouter.register('user', UserCreateViewSet)
ContentRouter.register('organizacao', OrganizacaoViewSet)
