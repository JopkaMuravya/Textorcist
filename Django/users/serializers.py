from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['record']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        if not UserProfile.objects.filter(user=user).exists():
            if profile_data:
                UserProfile.objects.create(user=user, **profile_data)
            else:
                UserProfile.objects.create(user=user)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        if profile_data:
            profile, created = UserProfile.objects.get_or_create(user=instance)
            for key, value in profile_data.items():
                setattr(profile, key, value)
            profile.save()

        return instance