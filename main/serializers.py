from rest_framework import serializers
from .models import Profile 

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username') 
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'user_type', 'company', 'department', 'title', 'first_name', 'last_name', 'email', 'username', 'image_url']

    def get_image_url(self, obj):
        if obj.image and obj.image.photo:
            return obj.image.photo.url 
        return None 
