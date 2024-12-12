from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin

class UserManager(UserManager):
   def _create_user(self, email, password, **extra_fields):
       email = self.normalize_email(email)
       user = self.model(email=email, **extra_fields)
       user.set_password(password)
       user.save(using=self._db)
       return user
   def create_user(self, email, password=None, **extra_fields):
       extra_fields.setdefault("is_staff", False)
       extra_fields.setdefault("is_superuser", False)
       return self._create_user(email, password, **extra_fields)
   def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)
       if extra_fields.get("is_staff") is not True:
           raise ValueError("Superuser must have is_staff=True.")
       if extra_fields.get("is_superuser") is not True:
           raise ValueError("Superuser must have is_superuser=True.")
       return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField("メールアドレス", unique=True)
   fullname = models.CharField("氏名", max_length=50)    
   zipcode=models.CharField(max_length=8, blank=True, null=True)
   address=models.CharField(max_length=100, blank=True, null=True)
   phone=models.CharField(max_length=11, blank=True, null=True)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   objects = UserManager()
   USERNAME_FIELD = "email"
   EMAIL_FIELD = "email"
   REQUIRED_FIELDS = []
   class Meta:
       verbose_name = ("user")
       verbose_name_plural = ("users")
   def clean(self):
       super().clean()
       self.email = self.__class__.objects.normalize_email(self.email)
