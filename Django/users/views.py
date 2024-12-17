from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import json

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

class GetRecordView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(UserProfile, user=user)
        return Response({"record": profile.record}, status=status.HTTP_200_OK)


class UpdateRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, username):
        try:
            user = get_object_or_404(User, username=username)
            profile = get_object_or_404(UserProfile, user=user)

            data = json.loads(request.body)
            new_record = data.get("record")

            if new_record is None:
                return JsonResponse({"error": "Record value is required"}, status=400)

            if new_record > profile.record:
                profile.record = new_record
                profile.save()

            return JsonResponse({"message": "Record updated successfully", "record": profile.record}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)