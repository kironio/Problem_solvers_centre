from django.db import models
from django.contrib import auth
from django.urls import reverse
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    # def get_absolute_url(self):
    #     return reverse("Solver_detail", kwargs={"pk": self.pk})
