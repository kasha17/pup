from django.db import models

# Create your models here.


class Base(models.Model):
    class Meta:
        abstract = True
        app_label = "parser"


class MainSites(Base):
    url = models.URLField(unique=True)
    SITE_TYPES = [
        ('txt', 'TXT'),
        ('php', 'PHP'),
        ('xml', 'XML'),
        ('ch', 'CH'),
        ('csv', 'CSV')
    ]
    type = models.CharField(max_length=3, choices=SITE_TYPES, default='txt')


class MalwareSites(Base):
    url = models.URLField(unique=True)


class PhishingSites(Base):
    url = models.URLField(unique=True)
