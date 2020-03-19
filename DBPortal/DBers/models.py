from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    account_type = models.CharField(blank=False,
                                    max_length=5,
                                    choices={('Staff', 'Staff'), ('DBer', 'DBer')},
                                    default='DBer')


class State(models.Model):
    name = models.CharField(max_length=20)


class City(models.Model):
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State, related_name='cities', on_delete=models.CASCADE)


class DBer(models.Model):
    user = models.OneToOneField(User, related_name='DBer', on_delete=models.CASCADE)
    aadhaar = models.PositiveIntegerField(validators=[MinValueValidator(12), MaxValueValidator(12)],
                                          blank=False)
    dob = models.DateField(blank=False)
    gender = models.CharField(max_length=6, choices={('Male', 'Male'), ('Female', 'Female')})
    state = models.ForeignKey(State,
                              null=True,
                              related_name='DBers',
                              on_delete=models.SET_NULL)
    city = models.ForeignKey(City,
                             null=True,
                             related_name='DBers',
                             on_delete=models.SET_NULL)


class Staff(models.Model):
    user = models.OneToOneField(User, related_name='Staff', on_delete=models.CASCADE)
    state = models.ForeignKey(State,
                              null=True,
                              related_name='Staff',
                              on_delete=models.SET_NULL)
    city = models.ForeignKey(City,
                             null=True,
                             related_name='Staff',
                             on_delete=models.SET_NULL)
