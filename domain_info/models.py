from django.db import models

# Create your models here.
class Domain_Info(models.Model):
    domain = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)
    open_ports = models.CharField(max_length=255)
    technology = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255, null=True)
    lookup = models.CharField(max_length=255, null=True)
    urls = models.CharField(max_length=255, null=True)
    directories = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain 
