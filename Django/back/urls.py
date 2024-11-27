from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet, LeaderboardAPIView, GetRecordView, UpdateRecordView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/get-record/<str:username>/', GetRecordView.as_view(), name='get_record'),
    path('api/update-record/<str:username>/', UpdateRecordView.as_view(), name='update_record'),
]