from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='images', blank=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=99, blank=True)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def save_profile(self):
        return self.save()

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @classmethod
    def delete_profile(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_profile_by_website(cls, website):
        search_results = cls.objects.filter(website=website).all()
        return search_results


class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=199, blank=False, null=False)
    description = models.TextField()
    tags = models.TextField(blank=True)
    screenshot_1 = CloudinaryField('screenshots')
    screenshot_2 = CloudinaryField('screenshots')
    screenshot_3 = CloudinaryField('screenshots')






