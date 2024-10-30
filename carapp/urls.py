from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import OwnerViewSet, CarViewSet, register_user, login_user

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
