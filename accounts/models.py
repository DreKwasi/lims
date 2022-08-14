from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Custom Account to define create user commands
class MyAccountManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, email, username, password=None
    ):
        """
        Creates a new user and assign the expected variables to them
        """
        if not email:
            raise ValueError("Users must have a valid email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        first_name,
        last_name,
        email,
        username,
        password=None,
    ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


# Custom User Model Inheriting from the AbstractBaseUser
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        max_length=100, unique=True, verbose_name="email address"
    )
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does a User Have A specific Permission?"
        return self.is_admin

    def has_module_perms(self, add_label):
        "Does the user have permissions to view the app `app_label`?"
        return True


class Facility(models.Model):
    facility_name = models.CharField(max_length=100, unique=True, null=True)
    facility_location = models.CharField(max_length=100, null=True, blank=True)
