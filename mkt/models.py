from django.db import models
from django.contrib.auth.models import User
from directory.models import Company
from django.utils import timezone

# Model of Campaign
class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name_campa = models.CharField(max_length=200, blank=False, default='')
    subject = models.CharField(max_length=200, blank=False, default='')
    body = models.TextField(blank=False, default='')
    url_body = models.CharField(max_length=200, blank=True, default='')
    state = models.CharField(max_length=200, blank=True, default='')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name_campa

# Model of StatCampa
class Statcampa(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_DEFAULT, default=1)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    body_comment = models.TextField(blank=True, default='')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.company.email