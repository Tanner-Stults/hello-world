from django.contrib import admin
from rango.models import Category, Page, WorkExperience, Painting, Education
from rango.models import UserProfile
from image_cropping import ImageCroppingMixin

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class WorkExperienceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
    #list_display = ('jobTitle', 'company', 'location', 'startDate', 'endDate', 'Info')

class UsersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'website':('website',)}

class UserProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
    #list_display = ('picture')
    #...

admin.site.register(UserProfile, UserProfileAdmin)
# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Painting)
admin.site.register(Education)