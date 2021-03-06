from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, Group
from image_cropping import ImageCropField, ImageRatioField
import os
from django.conf import settings
import datetime

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
    
class Cookies(models.Model):
    url = models.CharField(max_length=20000)
    user = models.CharField(max_length=2000)
    domain = models.CharField(max_length=2000, blank=True,)
    name = models.CharField(max_length=2000, blank=True,)
    content = models.CharField(max_length=2000, blank=True,)
    path = models.CharField(max_length=2000, blank=True,)
    
    class Meta:
      verbose_name_plural = "Cookies"
      ordering = ['domain']
    
    def __unicode__(self):
        return self.domain + ": " + self.name

class Items(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='profile_images', blank=True,)
    info = models.TextField(max_length=1000, blank=True)
    
    
    class Meta:
      verbose_name_plural = "Items"
      ordering = ['name']
    
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, editable=False)

    # The additional attributes we wish to include.

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='profile_images', blank=True,)
    coords = models.CharField(max_length=100, blank=True,)
    bgPicture = models.ImageField(upload_to='profile_bgimages', blank=True,)
    industry = models.CharField(max_length=200, blank=True,)
    currentCompany = models.CharField(max_length=200, blank=True,)
    currentPosition = models.CharField(max_length=200, blank=True,)
    currentLocation = models.CharField(max_length=200, blank=True,)
    previousCompany = models.CharField(max_length=200, blank=True,)
    previousPosition = models.CharField(max_length=200, blank=True,)
    education = models.CharField(max_length=400, blank=True,)
    linkedIn = models.URLField(blank=True)

    class Meta:
        ordering = ['user']

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.firstName + ' ' + self.lastName

class WorkExperience(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User, editable = False)

    # The additional attributes we wish to include.
    company = models.CharField(max_length=1000)
    jobTitle = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today, null=True)
    current = models.BooleanField(blank=True)
    info = models.TextField(max_length=1000, blank=True)

    class Meta:
        ordering = ['user']
        

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.company

class Education(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User, editable = False)


    SCHOOL_CHOICES = (('1','High School'), ('2', 'Community College'), ('3', 'College'), ('4', 'Technical Institute'))
    DEGREE_CHOICES = (('1', 'A.S.'),  ('2', 'A.A.'), ('3','A.A.S.'), ('4', 'B.A.'), ('5','B.S.'), ('6','B.F.A.'), ('7','B.B.A.'), ('8','B.Arch.'), ('9', 'M.F.A.'), ('10', 'M.A.'), ('11', 'M.S. '), ('12', 'M.A.'), ('13', 'M.Res.'), ('14', 'M.B.A.'), ('15', 'LL.M.'))
    # The additional attributes we wish to include.
    schoolType = models.CharField(max_length=200, choices=SCHOOL_CHOICES)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    major = models.CharField(max_length=200, blank = True)
    minor = models.CharField(max_length=200, blank = True)
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today, null=True)
    current = models.BooleanField(blank=True)
    grade = models.CharField(max_length=100, blank = True)
    info = models.CharField(max_length=1000, blank = True)
    activities = models.CharField(max_length=1000, blank = True)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['user']

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.school

class HCUser(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    userID = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    shoppinglist = models.CharField(max_length=2000, blank = True)
    #siteVisits = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    lastSiteVisit = models.CharField(max_length=200, blank = True)
    #storeVisits = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    lastStoreVisit = models.CharField(max_length=200, blank = True)
    #siteTime = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    #lastSiteTime = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    #storeTime = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)
    #lastStoreTime = models.CharField(max_length=200, choices = DEGREE_CHOICES, blank = True)

    class Meta:
        verbose_name_plural = "HCUsers"
        ordering = ['userID']

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.userID

class Painting(models.Model):

    # The additional attributes we wish to include.
    title = models.CharField(max_length=200,blank=True)
    date = models.DateField(blank=True)
    medium = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200,blank=True)
    art = models.ImageField(upload_to='paintings', default=os.path.join(settings.MEDIA_ROOT,'profile_bgimages','default.jpg'),)
    info = models.CharField(max_length=2000,blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title

