from django.db import models
from django.conf import settings
from django.utils import timezone  
from django.utils.http import urlquote  
from django.core.mail import send_mail  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name 

class Athlete(models.Model):
    name = models.CharField(max_length= 255)
    gender = models.CharField(max_length= 50)
    level = models.CharField(max_length= 50)
    age = models.IntegerField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey('app.Sport', null=True, blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="", null=True, blank=True)
    

    def __unicode__(self):
        return "%s" % self.name  



## Managing sign in:

class CustomeUserManager(BaseUserManager):

    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                            username=username,
                            is_staff=is_staff,
                            is_active=True,
                            is_superuser=is_superuser,
                            last_login=now,
                            date_joined=now,
                            **extra_fields
                            )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_user (self, email, username, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)    



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField('email address', max_length=200, unique=True)
    first_name = models.CharField('first name', max_length=50, null=True, blank=True)
    last_name = models.CharField('last name', max_length=50, null=True, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    # date_joined = models.DateTimeField('date joined', auto_now_add=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # User = get_user_model()
    objects = CustomeUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
