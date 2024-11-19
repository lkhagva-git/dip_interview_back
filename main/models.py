from django.db import models

from io import BytesIO
from django.core.files import File
from django.utils import timezone

from main.choices import *

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import uuid

import os


def path_and_rename(path):
    return os.path.join(path, uuid.uuid4().hex)


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to=path_and_rename("anket"))


class Anket(models.Model):
    level_count = models.CharField(max_length=500, verbose_name='Хэдэн ярилцлага хийх', null=True, blank=True)
    status = models.IntegerField(choices=ANKET_STATUS_CHOICES, verbose_name='Статус', null=True, blank=True)

    created_at = models.DateField(verbose_name='Үүссэн огноо', null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.CharField(max_length=500, verbose_name='Байгууллага', null=True, blank=True)
    department = models.CharField(max_length=500, verbose_name='Алба, хэлтэс', null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name='Албан тушаал', null=True, blank=True)
    ethnicity = models.CharField(max_length=500, verbose_name='Иргэний харьяалал', null=True, blank=True)
    family_name = models.CharField(max_length=500, verbose_name='Ургийн овог', null=True, blank=True)
    last_name = models.CharField(max_length=500, verbose_name='Эцэг эхийн нэр', null=True, blank=True)
    first_name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)
    register_number = models.CharField(max_length=500, verbose_name='Регистрийн дугаар', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Төрсөн огноо', null=True, blank=True)
    email = models.CharField(max_length=500, verbose_name='Имэйл', null=True, blank=True)
    phone =  models.CharField(max_length=20, verbose_name='Утасны дугаар', null=True, blank=True)
    phone2 =  models.CharField(max_length=20, verbose_name='Утасны дугаар 2', null=True, blank=True)
    city = models.CharField(max_length=500, verbose_name='Хот', null=True, blank=True) 
    district = models.CharField(max_length=500, verbose_name='Дүүрэг', null=True, blank=True) 
    address = models.CharField(max_length=500, verbose_name='Бүтэн хаяг', null=True, blank=True)

    sex = models.IntegerField(choices=SEX_CHOICES, verbose_name='Хүйс', null=True, blank=True)
    blood = models.IntegerField(choices=BLOOD_CHOICES, verbose_name='Цусны бүлэг', null=True, blank=True) 
    driver_type = models.IntegerField(choices=DRIVER_CHOICES, verbose_name='Жолооны ангилал', null=True, blank=True)
    driver_license = models.CharField(max_length=500, null=True, blank=True)
    medical = models.CharField(max_length=5000, verbose_name='Та эрүүл мэндийн хувьд анхаарах ямар нэгэн зовиур байгаа эсэх', null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.title} ({self.uuid})"

    class Meta:
        verbose_name = "Анкет"
        verbose_name_plural = "Анкет"
        ordering = ['-created_at']

class Family(models.Model):
    anket = models.ForeignKey(Anket, related_name='families', on_delete=models.CASCADE)
    what = models.IntegerField(choices=FAMILY_MEMBER_CHOICES, null=True, blank=True)
    first_name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)
    last_name = models.CharField(max_length=500, verbose_name='Овог', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Төрсөн огноо', null=True, blank=True)
    profession = models.CharField(max_length=500, verbose_name='Мэргэжил', null=True, blank=True)

    company = models.CharField(max_length=500, verbose_name='Байгууллага', null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name='Албан тушаал', null=True, blank=True)
    phone =  models.CharField(max_length=20, verbose_name='Утасны дугаар', null=True, blank=True)
    is_emergency_contact = models.BooleanField(default=False, verbose_name='Яаралтай үед холбогдох эсэх')
    is_live_together = models.BooleanField(default=False, verbose_name='Цуг амьдардаг эсэх')

class CareerContact(models.Model):
    anket = models.ForeignKey(Anket, related_name='career_contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)
    last_name = models.CharField(max_length=500, verbose_name='Овог', null=True, blank=True)
    company = models.CharField(max_length=500, verbose_name="Байгууллага", null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name='Албан тушаал', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Утасны дугаар', null=True, blank=True)
    email = models.CharField(max_length=500, verbose_name='Имэйл хаяг', null=True, blank=True)

class PriorCareer(models.Model):
    anket = models.ForeignKey(Anket, related_name='prior_careers', on_delete=models.CASCADE)
    company = models.CharField(max_length=500, verbose_name="Байгууллага", null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name="Албан тушаал", null=True, blank=True)
    salary = models.CharField(max_length=500, verbose_name="Цалингийн хэмжээ", null=True, blank=True)
    start_date = models.DateField(verbose_name="Орсон огноо", null=True, blank=True)
    end_date = models.DateField(verbose_name="Гарсан огноо", null=True, blank=True)
    leave_reason = models.CharField(max_length=500, verbose_name="Гарсан шалтгаан", null=True, blank=True)

class Award(models.Model):
    anket = models.ForeignKey(Anket, related_name='awards', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name='Гавьяа шагналын нэр', null=True, blank=True)
    year = models.DateField(verbose_name='Хүртсэн огноо', null=True, blank=True)
    where = models.CharField(max_length=500, verbose_name="Хаана ажиллах хугацаанд шагнагдсан", null=True, blank=True)

class Education(models.Model):
    anket = models.ForeignKey(Anket, related_name='educations', on_delete=models.CASCADE )
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default="MN")
    school_name = models.CharField(max_length=500, verbose_name="Сургуулийн нэр", null=True, blank=True)
    degree_level = models.IntegerField(choices=EDUCATION_CHOICES, verbose_name="Боловсролын зэрэг", null=True, blank=True)
    start_date = models.DateField(max_length=500, verbose_name="Элссэн он", null=True, blank=True)
    end_date = models.DateField(max_length=500, verbose_name="Төгссөн он", null=True, blank=True)
    profession = models.CharField(max_length=500, verbose_name="Эзэмшсэн мэргэжил", null=True, blank=True)
    gpa = models.CharField(max_length=500, verbose_name="Үнэлгээ", null=True, blank=True)

class Language(models.Model):
    anket = models.ForeignKey(Anket, related_name='languages', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Нэр", null=True, blank=True)
    listening= models.IntegerField(choices=PERCENTAGE_CHOICES, verbose_name="Сонсоод ойлгох чадвар", null=True, blank=True)
    reading = models.IntegerField(choices=PERCENTAGE_CHOICES, verbose_name="Уншаад ойлгох чадвар", null=True, blank=True)
    writing = models.IntegerField(choices=PERCENTAGE_CHOICES, verbose_name="Бичих чадвар", null=True, blank=True)
    speaking = models.IntegerField(choices=PERCENTAGE_CHOICES, verbose_name="Ярих чадвар", null=True, blank=True)

class Skill(models.Model):
    anket = models.ForeignKey(Anket, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)
    duration = models.CharField(max_length=100, verbose_name="Хугацаа", null=True, blank=True)
    award = models.CharField(max_length=500, verbose_name="Зэрэг, шагналтай эсэх", null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, verbose_name='Хэрэглэгчийн төрөл', default=0)
    company = models.CharField(max_length=500, verbose_name="Байгууллага", null=True, blank=True)
    department = models.CharField(max_length=500, verbose_name="Алба хэлтэс", null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name="Албан тушаал", null=True, blank=True)
    first_name = models.CharField(max_length=500, verbose_name="Нэр", null=True, blank=True)
    last_name = models.CharField(max_length=500, verbose_name="Овог", null=True, blank=True)
    email = models.CharField(max_length=500, verbose_name='Имэйл хаяг', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        return super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class Interview(models.Model):
    anket = models.ForeignKey(Anket, related_name='interviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, verbose_name="Хэд дэх ярилцлага", null=True, blank=True)
    status = models.IntegerField(choices=INTERVIEW_STATUS_CHOICES, verbose_name="Ярилцлагийн статус", null=True, blank=True)

# obeselete
    last_name = models.CharField(max_length=500, verbose_name='Овог', null=True, blank=True)
    first_name = models.CharField(max_length=500, verbose_name='Нэр', null=True, blank=True)

    interviewed_date = models.DateField(verbose_name='Ярилцлага хийсэн огноо', null=True, blank=True)

# obeselete
    company = models.CharField(max_length=500, verbose_name='Байгууллага', null=True, blank=True)
    department = models.CharField(max_length=500, verbose_name='Алба хэлтэс', null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name='Албан тушаал', null=True, blank=True)

    pros = models.CharField(max_length=1000, verbose_name='Анхаарал татсан чадварууд', null=True, blank=True)
    cons = models.CharField(max_length=1000, verbose_name='Ажиглагдсан сул тал', null=True, blank=True)
    
    main_overall = models.CharField(max_length = 1000, verbose_name ='Ерөнхий дүгнэлт', null=True, blank=True)
    
    conclution_points = models.IntegerField(verbose_name='Нэгдсэн дүгнэлт (оноо)', null=True, blank=True)

# obeselete
    possible_date = models.DateField(max_length=500, verbose_name ='Ажилд орох боломжтой огноо', null=True, blank=True)

    additional_note = models.CharField(max_length = 1000, verbose_name ='Нэмэлт тайлбар/тэмдэглэгээ', null=True, blank=True)

    communication  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Харилцаа өөрийгөө илэрхийлэх чадвар", null=True, blank=True)
    appearance  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Гадаад төрх", null=True, blank=True)
    logic_skill  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Асуултад хариулж буй байдал", null=True, blank=True)
    attitude  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Хандлага", null=True, blank=True)
    independence  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Идэвх санаачлага", null=True, blank=True)
    responsibility  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Өөрийгөө хөгжүүлэх зан чанар", null=True, blank=True)
    leadership  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Манлайлал болон багаар ажиллах", null=True, blank=True)
    knowledge  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Мэдлэг, авъяас", null=True, blank=True)
    overall_score  = models.IntegerField(choices=ASSIGN_CHOICES, verbose_name="Нэгдсэн дүгнэлт", null=True, blank=True)


    def save(self, *args, **kwargs):
        return super(Interview, self).save(*args, **kwargs)

class Desicion(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desicion_type = models.IntegerField(choices=DESICION_CHOICES, verbose_name="Шийдвэрийн төрөл", null=True, blank=True)
    created_at = models.DateField(verbose_name='Үүссэн огноо', null=True, blank=True)
    
class Schedule(models.Model):
    anket = models.ForeignKey(Anket, related_name='schedules', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, verbose_name ='Хаяг', null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    





