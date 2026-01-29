from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = CloudinaryField('image', folder='images/')
    github = models.URLField(blank = True)
    live = models.BooleanField(blank = True)

    def __str__(self):
        return self.title

class SkillProgress(models.Model):
    name = models.CharField(max_length = 100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class SkillLearned(models.Model):
    name = models.CharField(max_length = 100)
    svg = models.URLField(blank = True)

    def __str__(self):
        return self.name

class Education(models.Model):
    instiitute = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 150)
    description = models.TextField()

    def __str__(self):
        return self.instiitute

class Logo(models.Model):
    logoTitle = models.CharField(max_length = 5)

    def __str__(self):
        return self.logoTitle

class ProfilePicture(models.Model):
    sketch = CloudinaryField('image', folder='images/')
    original = CloudinaryField('image', folder='images/')

    def __str__(self):
        return f"Profile Image {self.id}"

class WelcomeNote(models.Model):
    name = models.CharField(max_length=125)
    line1 = models.TextField()
    line2 = models.TextField()

    def __str__(self):
        return self.name

class MoreList(models.Model):
    more = models.CharField(max_length=50)
    file = models.CharField(max_length=50)

    def __str__(self):
        return self.more

class Experience(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.title