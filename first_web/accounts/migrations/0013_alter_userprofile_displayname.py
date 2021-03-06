# Generated by Django 3.2.6 on 2021-09-05 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210905_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='displayName',
            field=models.CharField(default=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=30, unique=True),
        ),
    ]
