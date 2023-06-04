from django.db import models
from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
# Create your models here.


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length=254, blank=True, null=True)

    class meta:
        managed = False
        db_table = 'users'

class Project(models.Model):
    project_id = models.BigIntegerField(primary_key=True)
    project_name = models.CharField(max_length=254, blank=True, null=True)
    org_name = models.CharField(max_length=254, blank=True, null=True)
    owner_id = models.BigIntegerField()

    class meta:
        managed = False
        db_table = 'project'

class Dataset(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dataset_name = models.CharField(max_length=254, blank=True, null=True)
    project_id = models.BigIntegerField()

    class meta:
        managed = False
        db_table = 'dataset'

class Organizations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=254, blank=True, null=True)

    class meta:
        managed = False
        db_table = 'organization'
