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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@login_required
def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def get_items(request):
    # items = Item.objects.all()
    # serializer = ItemSerializer(items, many=True)
    # return Response(serializer.data)

    return Response("Heelloooo world API your is working lkhagva!!!!!!")