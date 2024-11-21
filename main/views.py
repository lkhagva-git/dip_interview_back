import logging
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
from django.core.mail import send_mail
from django.conf import settings

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
        ankets = Anket.objects.filter(status=0)
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

        serializer = InterviewGetSerializer(interviews, many=True)
        return Response(serializer.data)
    except Anket.DoesNotExist:
        return Response({"error": "Candidate not found"}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def interview_detail(request, pk):
    """
    Retrieve the candidate's interview detail.
    """
    try:
        interviews = Interview.objects.get(pk=pk)
        serializer = InterviewDetailSerializer(interviews)
        return Response(serializer.data)
    except Interview.DoesNotExist:
        return Response({"error": "Interview not found"}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_list(request):
    """
    Retrieve the profile list.
    """
    try:
        profiles = Profile.objects.exclude(user_type=2)

        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)

    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAnket(request):
    serializer = AnketSerializer(data=request.data)
    
    if serializer.is_valid():
        anket = serializer.save()

        related_data = request.data.get('related', {})

        families = related_data.get('families', [])
        for family_data in families:
            Family.objects.create(anket=anket, **family_data)

        contacts = related_data.get('contacts', [])
        for contact_data in contacts:
            CareerContact.objects.create(anket=anket, **contact_data)

        prior_careers = related_data.get('prior_careers', [])
        for career_data in prior_careers:
            PriorCareer.objects.create(anket=anket, **career_data)

        awards = related_data.get('awards', [])
        for award_data in awards:
            Award.objects.create(anket=anket, **award_data)

        education_entries = related_data.get('education', [])
        for education_data in education_entries:
            Education.objects.create(anket=anket, **education_data)

        languages = related_data.get('languages', [])
        for language_data in languages:
            Language.objects.create(anket=anket, **language_data)

        skills = related_data.get('skills', [])
        for skill_data in skills:
            Skill.objects.create(anket=anket, **skill_data)

        return Response({'message': 'Анкет successfully created!', 'anket': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def conduct_interview(request):
    """
    After conducted interview, update interview object accordingly.
    """
    serializer = InterviewPostSerializer(data=request.data)

    if serializer.is_valid():
        try:
            inter_id = request.data.get('inter_id')
            inter = Interview.objects.get(pk=inter_id)

            interviewed_date = datetime.datetime.now().date()

            for attr, value in serializer.validated_data.items():
                setattr(inter, attr, value)
            inter.interviewed_date = interviewed_date
            inter.is_completed = True
            inter.save()

            if inter.status == 1:
                rest_interviews = Interview.objects.filter(level__gt=inter.level, anket=inter.anket)
                for item in rest_interviews:
                    item.is_completed = True
                    item.save()

            if inter.is_final:
                if inter.status == 2:
                    inter.anket.status = 1  
                else:
                    inter.anket.status = 2
                inter.anket.save() 

            send_text_status = INTERVIEW_STATUS_CHOICES[inter.status]

            if inter.status == 0:
                try:
                    next_inter = Interview.objects.get(anket=inter.anket, level=inter.level + 1)
                    profile = Profile.objects.get(user=next_inter.user) 
                    send_text_1 = f"{inter.interviewed_date}-ний өдрийн ярилцлагын үр дүн {send_text_status[1]} төлөвтэй амжилттай явагдсан тул таньд дараах ажил горилогч санал болгогдлоо. http://localhost:3000/candidate/{inter.anket.id}"
                    send_interview_email(profile.email, "Ажил горилогч санал болгох", send_text_1)
                except (Interview.DoesNotExist, Profile.DoesNotExist) as e:
                    logging.error(f"Next interview or profile not found: {str(e)}")
                    return Response({'error': 'Next interview or profile not found'}, status=status.HTTP_404_NOT_FOUND)

            try:
                send_text_2 = "Эрхэм " + inter.anket.last_name + " " + inter.anket.first_name + " танд энэ өдрийн мэндийг хүргэе. Таны " + str(inter.interviewed_date) + "-ний өдрийн ярилцлагын үр дүн "  + send_text_status[1] + " төлөвтэй амжилттай явагдлаа."
                send_interview_email(inter.anket.email, "Ярилцлагын үр дүн", send_text_2)
            except Exception as e:
                logging.error(f"Failed to send email to candidate: {str(e)}")
                return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Interview updated successfully'}, status=status.HTTP_200_OK)
        
        except Interview.DoesNotExist:
            return Response({'error': 'Interview not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(f"Unexpected error occurred: {str(e)}")
            return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_interview_plan(request):
    """
    Create interview plan by creating interview objects.
    """
    try:
        employee_ids = request.data.get('employee_ids')
        anket_id = request.data.get('anket_id')

        if not employee_ids or not anket_id:
            return Response({'error': 'Employee IDs and Anket ID are required.'}, status=status.HTTP_400_BAD_REQUEST)

        anket = Anket.objects.get(pk=anket_id)

        for i, employee_id in enumerate(employee_ids, start=1):
            profile = Profile.objects.get(pk=employee_id)
            is_final = (i == len(employee_ids))
            Interview.objects.create(anket=anket, user=profile.user, level=i, is_final=is_final)

        return Response({'message': 'Interview plans created successfully.'}, status=status.HTTP_201_CREATED)
    
    except Anket.DoesNotExist:
        return Response({'error': 'Anket not found.'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_schedule(request):
    """
    Create interview schedule
    """
    try:
        candidate_id = request.data.get('candidate_id')
        if not candidate_id:
            return Response({'error': 'Candidate ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            anket = Anket.objects.get(pk=candidate_id)
        except Anket.DoesNotExist:
            return Response({'error': 'Anket not found.'}, status=status.HTTP_404_NOT_FOUND)

        inter_id = request.data.get('inter_id')
        if not inter_id:
            return Response({'error': 'Interview ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            interview = Interview.objects.get(pk=inter_id)
        except Interview.DoesNotExist:
            return Response({'error': 'Interview not found.'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        created_at = timezone.now().date()

        date_time = request.data.get('date_time')
        if not date_time:
            return Response({'error': 'Date and time are required.'}, status=status.HTTP_400_BAD_REQUEST)

        address = request.data.get('address', '')

        try:
            schedule = Schedule.objects.create(
                anket=anket,
                user=user,
                interview=interview,
                address=address,
                date_time=date_time,
                created_at=created_at
            )
        except Exception as e:
            return Response({'error': f'Failed to create schedule: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        interview.is_scheduled = True
        interview.save()

        try:
            profile = Profile.objects.get(user=user)
            send_text = (
                f"Эрхэм хүндэт {anket.last_name} {anket.first_name} таны ажлын ярилцлага товлогдлоо. "
                f"Ярилцлага хийгч: {profile.title} албан тушаалтай {profile.last_name} {profile.first_name}, "
                f"Байршлын хаяг: {schedule.address}, Огноо: {str(schedule.date_time)}"
            )
            send_interview_email(anket.email, "Ярилцлагын тов", send_text)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile for user not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Failed to send email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(ScheduleSerializer(schedule).data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedule_list(request):
    """
    Retrieve the schedule list where the related interview's is_completed field is False.
    """
    schedules = Schedule.objects.filter(interview__is_completed=False)

    serializer = ScheduleSerializer(schedules, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


def send_interview_email(recipient_email, subject, message):
    """
    Helper function, email sender
    """
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return {"message": "Email sent successfully", "status": True}
    except Exception as e:
        return {"message": f"Failed to send email: {str(e)}", "status": False}
    

def send_test_email(request=None):
    send_mail(
        'Test Subject',
        'This is a test message from Django using Mailtrap.',
        settings.DEFAULT_FROM_EMAIL,
        ['sukhochirlkhagva@gmail.com'],
        fail_silently=False,
    )
  