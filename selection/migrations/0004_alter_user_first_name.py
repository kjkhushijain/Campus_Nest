# Generated by Django 4.2.6 on 2023-10-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_student_no_dues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]