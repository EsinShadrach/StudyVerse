from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=100)
    tag = models.SlugField(max_length=20, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    law_1 = models.TextField(max_length=20, blank=True, null=True)
    law_2 = models.TextField(max_length=20, blank=True, null=True)
    law_3 = models.TextField(max_length=20, blank=True, null=True)
    Formula_1 = models.TextField(max_length=20, blank=True, null=True)
    Param_1 = models.TextField(max_length=200, blank=True, null=True)
    Formula_2 = models.TextField(max_length=20, blank=True, null=True)
    Param_2 = models.TextField(max_length=200, blank=True, null=True)
    Formula_3 = models.TextField(max_length=20, blank=True, null=True)
    Param_3 = models.TextField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ['tag']
        