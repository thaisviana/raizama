from .content import ContentViewSet
from .user import UserCreateViewSet
from .produtor import ProdutorViewSet
from contrib.router import HybridRouter


ContentRouter = HybridRouter()
ContentRouter.register('content', ContentViewSet)
ContentRouter.register('user', UserCreateViewSet)
ContentRouter.register('produtor', ProdutorViewSet)
