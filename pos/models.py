from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator


# Model for branchs
class Branch(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, blank=False, default='')
    description = models.TextField(blank=False, default='')
    address = models.CharField(max_length=50, blank=False, default='')
    #location = 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='') # validators should be a list
    
    def __str__(self):
        return self.name

    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    image = models.ImageField('image product',
                               upload_to=user_directory_path,
                               null=True,
                               blank=True,
                               )
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name


# Model for products
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, blank=False, default='')
    code = models.IntegerField(blank=False, default='')
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, max_length=50, blank=False, default='')
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, max_length=50, blank=False, default='')
    description = models.TextField(blank=False, default='')
    amount = models.IntegerField(blank=False, default='')

    def user_directory_path(instance, filename):
        return 'products/user_{0}/{1}'.format(instance.owner.id, filename)
    image = models.ImageField('image product',
                               upload_to=user_directory_path,
                               null=True,
                               blank=True,
                               )
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name

# Model for services
class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, blank=False, default='')
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, max_length=50, blank=False, default='')
    description = models.TextField(blank=False, default='')
    #amount = models.IntegerField(max_length=6, blank=False, default='') #algo para citas

    def user_directory_path(instance, filename):
        return 'static/products/user_{0}/{1}'.format(instance.owner.id, filename)
    image = models.ImageField('image product',
                               upload_to=user_directory_path,
                               null=True,
                               blank=True,
                               )
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name