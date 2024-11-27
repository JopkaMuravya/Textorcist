from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import UserProfile


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = UserProfile.objects.select_related('user').all()
        data = [
            {
                'username': user.user.username,
                'email': user.user.email,
                'record': user.record,
            }
            for user in users
        ]
        return Response(data, status=status.HTTP_200_OK)


class LeaderboardAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        leaderboard = UserProfile.objects.select_related('user').order_by('-record')
        data = [
            {
                "name": profile.user.username,
                "record": profile.record
            }
            for profile in leaderboard
        ]
        return Response(data)