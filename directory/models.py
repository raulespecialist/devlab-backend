from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator


# Model of User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField('profile picture', upload_to='static/avatars/',
                               null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='') # validators should be a list


    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar = "static/avatars/default.png"

    def __str__(self):
        return self.user.username

# Model of Companies
class Company(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_DEFAULT, default='robot')
    name_company = models.CharField(max_length=50, blank=False, default='')
    manager_fname = models.CharField(max_length=30, blank=False, default='')
    manager_lname = models.CharField(max_length=30, blank=True, default='')
    fb_url = models.CharField(max_length=30, blank=True, default='')
    tw_url = models.CharField(max_length=30, blank=True, default='')
    rfc = models.CharField(max_length=20, blank=True, default='')
    scope = models.CharField(max_length=50, blank=True, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='') # validators should be a list
    email = models.EmailField(max_length=70,blank=False,unique=True)
    web = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    private = models.BooleanField(blank=True, default=False)
    newsletter = models.BooleanField(default=True)
    score = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name_company

# Model of Comments
class Comment(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rating = models.IntegerField()
    body_comment = models.TextField(blank=True, default='')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.owner
