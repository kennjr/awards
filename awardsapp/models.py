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
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, by {self.creator.username}'

    def save_project(self):
        return self.save()

    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def delete_projects(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_project_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_project_by_name(cls, name):
        search_results = cls.objects.filter(name=name).all()
        return search_results


class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(blank=False, null=False)
    content = models.IntegerField(blank=False, null=False)
    usability = models.IntegerField(blank=False, null=False)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project.name}, {self.reviewer.username}'

    def add_rating(self):
        return self.save()

    @classmethod
    def get_all_ratings(cls):
        return cls.objects.all()

    @classmethod
    def delete_rating(cls, r_id):
        return cls.objects.filter(id=r_id).delete()

    @classmethod
    def get_rating_by_id(cls, r_id):
        return cls.objects.filter(id=r_id).all()

    @classmethod
    def search_rating_by_reviewer_id(cls, uid):
        search_results = cls.objects.filter(reviewer__id=uid).all()
        return search_results


class AvgRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, unique=True)
    design = models.IntegerField(blank=False, null=False, default=0)
    content = models.IntegerField(blank=False, null=False, default=0)
    usability = models.IntegerField(blank=False, null=False, default=0)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project.name}'

    def add_rating(self):
        return self.save()

    @classmethod
    def get_all_avg_ratings(cls):
        return cls.objects.all()

    @classmethod
    def delete_avg_rating(cls, r_id):
        return cls.objects.filter(id=r_id).delete()

    @classmethod
    def get_avg_rating_by_id(cls, r_id):
        return cls.objects.filter(id=r_id).all()

    @classmethod
    def search_avg_rating_by_project_id(cls, uid):
        search_results = cls.objects.filter(project__id=uid).all()
        return search_results



