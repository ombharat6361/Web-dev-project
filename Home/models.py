from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

# class User(AbstractUser):

#     class Types(models.TextChoices):
#         PROFESSIONAL="Professional","PROFESSIONAL"
#         USER="USER","User"

#     type=models.CharField(max_length=50,choices=Types.choices,default=Types.USER)

#     username=models.CharField(max_length=250,unique=True)

#     password=models.CharField(max_length=250)

# class Professional(User):
#     class Meta:
#         proxy=True

# class NormalUser(User):
#     class Meta:
#         proxy=True

class Blog(models.Model):
    title=models.CharField(max_length=100)
    subheading=models.CharField(max_length=500)
    description=models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Blog"
        ordering=['-created_at']

# class Topic(models.Model):
#     name=models.CharField(max_length=200)

    
#     def __str__(self):
#         return self.name



class Room(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.CharField(max_length=200)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    class Meta:
        ordering = ['-updated','-created']

