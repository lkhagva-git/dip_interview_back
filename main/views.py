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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def candidates_data(request):
    """
    Retrieve the candidates' data.
    """
    try:
        # statusaar ylgah
        ankets = Anket.objects.all()
        serializer = AnketSerializer(ankets, many=True)
        return Response(serializer.data)
    except Anket.DoesNotExist:
        return Response({"error": "Candidates not found"}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_application(request, pk):
    """
    Retrieve the candidate's detail data including all related information.
    """
    try:
        candidate = Anket.objects.get(pk=pk)
        serializer = CandidateDetailSerializer(candidate)
        return Response(serializer.data)
    except Anket.DoesNotExist:
        return Response({"error": "Candidate not found"}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def interview_history(request, pk):
    """
    Retrieve the candidate's interview history.
    """
    try:
        anket = Anket.objects.get(pk=pk)
        interviews = Interview.objects.filter(anket=anket)

        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data)
    except Anket.DoesNotExist:
        return Response({"error": "Candidate not found"}, status=404)

    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAnket(request):
    # Deserialize the incoming data
    serializer = AnketSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the anket instance
        anket = serializer.save()

        # Handle the related models if present in the request data
        related_data = request.data.get('related', {})

        # Create related Family members
        families = related_data.get('families', [])
        for family_data in families:
            Family.objects.create(anket=anket, **family_data)

        # Create related CareerContact entries
        contacts = related_data.get('contacts', [])
        for contact_data in contacts:
            CareerContact.objects.create(anket=anket, **contact_data)

        # Create related PriorCareer entries
        prior_careers = related_data.get('prior_careers', [])
        for career_data in prior_careers:
            PriorCareer.objects.create(anket=anket, **career_data)

        # Create related Awards
        awards = related_data.get('awards', [])
        for award_data in awards:
            Award.objects.create(anket=anket, **award_data)

        # Create related Education entries
        education_entries = related_data.get('education', [])
        for education_data in education_entries:
            Education.objects.create(anket=anket, **education_data)

        # Create related Languages
        languages = related_data.get('languages', [])
        for language_data in languages:
            Language.objects.create(anket=anket, **language_data)

        # Create related Skills
        skills = related_data.get('skills', [])
        for skill_data in skills:
            Skill.objects.create(anket=anket, **skill_data)

        return Response({'message': 'Анкет successfully created!', 'anket': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_interview(request):
    serializer = InterviewPostSerializer(data=request.data)

    if serializer.is_valid():
        try:
            user = request.user
            anket_id = request.data.get('candidate_id')
            anket = Anket.objects.get(pk=anket_id)

            level = Interview.objects.filter(anket=anket).count() + 1

            interviewed_date = datetime.datetime.now().date()

            interview = serializer.save(user=user, anket=anket, level=level, interviewed_date=interviewed_date)

            return Response(InterviewSerializer(interview).data, status=status.HTTP_201_CREATED)

        except Anket.DoesNotExist:
            return Response({'error': 'Anket not found.'}, status=status.HTTP_400_BAD_REQUEST)

    # If the data is not valid, return the validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
