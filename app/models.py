from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=10,primary_key=True)