# Generated by Django 3.2.6 on 2021-08-29 23:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/avatars/', verbose_name='profile picture')),
                ('phone_number', models.CharField(blank=True, default='', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(default='', max_length=50)),
                ('manager_fname', models.CharField(default='', max_length=30)),
                ('manager_lname', models.CharField(blank=True, default='', max_length=30)),
                ('fb_url', models.CharField(blank=True, default='', max_length=30)),
                ('tw_url', models.CharField(blank=True, default='', max_length=30)),
                ('rfc', models.CharField(blank=True, default='', max_length=20)),
                ('scope', models.CharField(blank=True, default='', max_length=50)),
                ('phone_number', models.CharField(blank=True, default='', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('web', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('private', models.BooleanField(blank=True, default=False)),
                ('newsletter', models.BooleanField(default=True)),
                ('score', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default='robot', on_delete=django.db.models.deletion.SET_DEFAULT, to='directory.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('body_comment', models.TextField(blank=True, default='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.company')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.userprofile')),
            ],
        ),
    ]
