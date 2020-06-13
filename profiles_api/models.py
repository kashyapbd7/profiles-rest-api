from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# class UserProfileManager(BaseUserManager):
#     """Model manager fo custom user profiles"""
#
#     def create_user(self, email, name, password= None):
#         """For all the users"""
#
#         if not email:
#             raise ValueError("User must enter valid email")
#
#         email = self.email.normalize_email(email)
#         user = self.model(name = name, email = email)
#
#         user.set_password(password)
#         user.save(using = self._db)
#
#         return user
#
#
#     def create_superuser(self, email, name, password):
#         """"Manager for superuser"""
#
#         user = self.create_user(email ,name , password)
#
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using = self._db)
#
#         return user
#
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email,name,password=None):
        """Creating the user Profile"""
        if not email:
            raise ValueError("User meust have email address")

        email = self.normalize_email(email)
        user = self.model(email = email,name = name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name,password):
        """Creating and save new superuser"""
        user= self.create_user(email,name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Creating user profile model"""

    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """To retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Returning Short name"""
        return self.name























# class UserProfileManager(BaseUserManager):
#     """Manager for user profiles"""
#
#     def create_user(self, email,name,password=None):
#         """Creating the user Profile"""
#         if not email:
#             raise ValueError("User meust have email address")
#
#         email = self.normalize_email(email)
#         user = self.model(email = email,name = name)
#
#         user.set_password(password)
#         user.save(using = self._db)
#
#         return user
#
#     def create_superuser(self, email, name,password):
#         """Creating and save new superuser"""
#         user= self.create_user(email,name, password)
#
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#         return user
#
# class UserProfile(AbstractBaseUser,PermissionsMixin):
#     """Database Model for user in the system """
#
#     email =  models.EmailField(max_length = 255, unique= True)
#     name = models.CharField(max_length= 255)
#     is_active = models.BooleanField(default= True)
#     is_staff = models.BooleanField(default= True)
#
#     objects = UserProfileManager()
#
#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = ["name"]
#
#     def get_full_name(self):
#         """Returning the full name of the user"""
#         return self.name
#
#     def get_sort_name(self):
#         """Returning the short name of the user"""
#         return self.name
