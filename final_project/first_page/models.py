from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Course(models.Model):
    course_id = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    number_Class_Days = models.CharField(max_length=80)
    extra_Assign = models.CharField(max_length=80)

class StudentSign(models.Model):
    student_id = models.CharField(max_length=7)
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length= 50)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
