from django.db import models
import uuid
from .manage import CustomUser
from django.contrib.auth.models import AbstractUser



class Member(AbstractUser):
    username=None
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUser()
    membership_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email