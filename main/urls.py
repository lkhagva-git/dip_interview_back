from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/items/', views.get_items, name='get_items'),
    # path('api/token/', views.login_view, name='login_view'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/smart_anket/', views.smart_anket, name='smart_anket'),
    path('api/test_access/', views.test_access, name='test_access'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)