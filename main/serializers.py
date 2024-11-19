from rest_framework import serializers
from .models import * 

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


class AnketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anket
        fields = '__all__'

    def validate(self, data):
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            if field not in data or data[field] in [None, '']:
                raise serializers.ValidationError({field: f'{field} is required and cannot be null or empty.'})
        return data

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class CareerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerContact
        fields = '__all__'

class PriorCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorCareer
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class CandidateDetailSerializer(serializers.ModelSerializer):
    families = FamilySerializer(many=True, read_only=True)
    career_contacts = CareerContactSerializer(many=True, read_only=True)
    prior_careers = PriorCareerSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Anket
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add any custom processing if necessary.
        return representation

class InterviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username') 
    department = serializers.CharField(source='user.profile.department') 
    title = serializers.CharField(source='user.profile.title') 
    first_name = serializers.CharField(source='user.profile.first_name') 
    last_name = serializers.CharField(source='user.profile.last_name') 

    class Meta:
        model = Interview
        fields = ['username', 'department', 'title', 'first_name', 'last_name', 'level', 'status', 'interviewed_date', 'main_overall']

class InterviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class InterviewPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = ['status', 'pros', 'cons', 'main_overall', 'conclution_points', 'additional_note', 'communication', 'appearance', 'logic_skill', 'attitude', 'independence', 'responsibility', 'leadership', 'knowledge', 'overall_score']

        