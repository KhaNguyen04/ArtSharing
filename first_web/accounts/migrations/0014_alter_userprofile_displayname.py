# Generated by Django 3.2.6 on 2021-09-05 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_userprofile_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='displayName',
            field=models.CharField(blank=True, default=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=30, unique=True),
        ),
    ]
