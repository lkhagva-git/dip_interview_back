# Generated by Django 5.1.3 on 2024-11-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_interview_is_scheduled_alter_image_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='is_final',
            field=models.BooleanField(default=False, verbose_name='Сүүлийн/Шийдвэрлэх ярилцлага эсэх'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='anket/64c0a37ffed348089855c2cf01791f1e'),
        ),
    ]
