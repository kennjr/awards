from django.contrib import admin

# Register your models here.
# This class determines how the admin dashboard will look
from awardsapp.models import Project, AvgRating, Rating, Profile


class ProjectAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('name', 'description',)
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('name', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class RatingAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('project', 'reviewer', 'design', 'content', 'usability')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('project', 'reviewer',)
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class ProfileAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('website', 'bio')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('website', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class AvgRatingAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('project', 'design', 'content', 'usability')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('project', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(AvgRating, AvgRatingAdmin)
admin.site.register(Profile, ProfileAdmin)
