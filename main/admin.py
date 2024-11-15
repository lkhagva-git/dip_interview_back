from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'photo')
    search_fields = ('uuid',)

@admin.register(Anket)
class AnketAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created_at', 'status')
    search_fields = ('title', 'company', 'first_name', 'last_name', 'register_number')
    list_filter = ('status', 'company', 'created_at')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('anket', 'first_name', 'last_name', 'what', 'is_emergency_contact')
    search_fields = ('first_name', 'last_name', 'anket__first_name', 'anket__last_name')
    list_filter = ('is_emergency_contact', 'is_live_together')

@admin.register(CareerContact)
class CareerContactAdmin(admin.ModelAdmin):
    list_display = ('anket', 'first_name', 'last_name', 'company', 'title')
    search_fields = ('first_name', 'last_name', 'company', 'title')

@admin.register(PriorCareer)
class PriorCareerAdmin(admin.ModelAdmin):
    list_display = ('anket', 'company', 'title', 'start_date', 'end_date')
    search_fields = ('company', 'title', 'anket__first_name', 'anket__last_name')
    list_filter = ('start_date', 'end_date')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('anket', 'name', 'year', 'where')
    search_fields = ('name', 'anket__first_name', 'anket__last_name')
    list_filter = ('year',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('anket', 'school_name', 'degree_level', 'start_date', 'end_date')
    search_fields = ('school_name', 'anket__first_name', 'anket__last_name')
    list_filter = ('degree_level', 'start_date', 'end_date')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('anket', 'name', 'listening', 'reading', 'writing', 'speaking')
    search_fields = ('name', 'anket__first_name', 'anket__last_name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('anket', 'name', 'duration', 'award')
    search_fields = ('name', 'anket__first_name', 'anket__last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'company', 'department', 'title')
    search_fields = ('user__username', 'first_name', 'last_name', 'company', 'department')
    list_filter = ('user_type', 'company', 'department')

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('anket', 'user', 'level', 'status', 'interviewed_date')
    search_fields = ('user__username', 'anket__first_name', 'anket__last_name')
    list_filter = ('status', 'interviewed_date')

@admin.register(Desicion)
class DesicionAdmin(admin.ModelAdmin):
    list_display = ('interview', 'user', 'desicion_type', 'created_at')
    search_fields = ('interview__anket__first_name', 'interview__anket__last_name', 'user__username')
    list_filter = ('desicion_type', 'created_at')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('anket', 'user', 'address', 'date_time', 'created_at')
    search_fields = ('user__username', 'anket__first_name', 'anket__last_name', 'address')
    list_filter = ('date_time', 'created_at')