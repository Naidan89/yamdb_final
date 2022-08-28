from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet,
                    CreateUserViewSet, GenreViewSet,
                    GetJWTTokenViewSet, ReviewViewSet,
                    TitlesViewSet, UserViewSet)


app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', CreateUserViewSet, basename='signup')
router.register('auth/token', GetJWTTokenViewSet, basename='token')
router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitlesViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews'
    r'/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls))
]
