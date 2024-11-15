import re
import datetime
import json

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status

from .models import *
from .serializers import *


@api_view(['GET'])
def get_items(request):

    return Response("Heelloooo world API your is working lkhagva!!!!!!")

@csrf_exempt
@api_view(['POST'])
def login_view(request):
    """
    Authenticate user and return token if credentials are valid.
    """

    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def smart_anket(request):
    """
    Check if the authenticated user's profile status is 2 or if they are an admin.
    """
    user = request.user
    print("user ----------------------------------->")
    print(user)
    return Response({"message": "Access granted"}, status=status.HTTP_200_OK)

    profile = getattr(user, 'profile', None)  # Safely access the profile if it exists

    # Check if profile exists and user has required status or is admin
    if profile and (profile.status == 2 or profile.is_admin):
        return Response({"message": "Access granted"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Access denied"}, status=status.HTTP_403_FORBIDDEN)


# Optional additional endpoint for testing access to smart_anket without profile restrictions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_access(request):
    """
    Example endpoint to test access with only authentication.
    """
    return Response({"message": "Authenticated access granted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_data(request):
    """
    Retrieve the authenticated user's profile data.
    """
    user = request.user
    try:
        profile = Profile.objects.get(user=user) 
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)