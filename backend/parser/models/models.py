from django.db import models

# Create your models here.


class MainSites(models.Model):
    url = models.URLField(unique=True)
    SITE_TYPES = [
        ('txt', 'TXT'),
        ('php', 'PHP'),
        ('xml', 'XML'),
        ('ch', 'CH'),
        ('csv', 'CSV')
    ]
    type = models.CharField(max_length=3, choices=SITE_TYPES, default='txt')


class MalwareSites(models.Model):
    url = models.URLField(unique=True)


class PhishingSites(models.Model):
    url = models.URLField(unique=True)
