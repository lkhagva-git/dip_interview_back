from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('api/items/', views.get_items, name='get_items'),
    # path('api/token/', views.login_view, name='login_view'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    path('api/profile_data/', views.profile_data, name='profile_data'),
    path('api/test_access/', views.test_access, name='test_access'),


    path('api/anket/', views.createAnket, name='createAnket'),
    path('api/candidates_data/', views.candidates_data, name='candidates_data'),
    path('api/job_application/<int:pk>/', views.job_application, name='job_application'),
    path('api/interview_history/<int:pk>/', views.interview_history, name='interview_history'),

    path('api/create_interview/', views.create_interview, name='create_interview'),
    path('api/profile_list/', views.profile_list, name='profile_list'),


    path('api/create_interview_plan/', views.create_interview_plan, name='create_interview_plan'),
    path('api/create_schedule/', views.create_schedule, name='create_schedule'),
    path('api/schedule_list/', views.schedule_list, name='schedule_list'),
    path('api/interview_detail/<int:pk>/', views.interview_detail, name='interview_detail'),


    path('send_test_email', views.send_test_email, name='send_test_email'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)