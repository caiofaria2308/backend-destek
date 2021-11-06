from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=1234):
        """
            Creates and saves a User with the given email and password
        """

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_supportuser(self, email, password):
        """
            Creates and saves a support user with the given email and password
        """
        user = self.create_user(email, password)
        user.support = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """
            Creates and saves a support user with the given email and password
        """
        user = self.create_user(email, password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(verbose_name="Full name", max_length=50)
    email = models.EmailField(verbose_name="Email address", unique=True)
    phone = models.CharField(verbose_name="cellphone number", unique=True, null=True, max_length=20)
    support = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

    def __str__(self) -> str:
        return self.name


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_support(self):
        """Is the user a member of support?"""
        return self.support

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin


class Setting(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    label = models.CharField(verbose_name="label of setting", max_length=255, unique=True)
    value = models.TextField(verbose_name="Value of setting")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['label']
