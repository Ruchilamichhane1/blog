from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)



class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    
def __str__(self):
        return self.all
    