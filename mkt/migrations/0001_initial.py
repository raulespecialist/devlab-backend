# Generated by Django 3.2.6 on 2021-09-04 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0005_auto_20210901_0159'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_campa', models.CharField(default='', max_length=200)),
                ('subject', models.CharField(default='', max_length=200)),
                ('body', models.TextField(default='')),
                ('url_body', models.CharField(blank=True, default='', max_length=200)),
                ('state', models.CharField(blank=True, default='', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statcampa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_comment', models.TextField(blank=True, default='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mkt.campaign')),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='directory.company')),
            ],
        ),
    ]
