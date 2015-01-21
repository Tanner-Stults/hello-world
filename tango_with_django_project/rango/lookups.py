from rango.models import Category, Page, UserProfile, WorkExperience, Education

from selectable.base import ModelLookup
from selectable.registry import registry

class UserProfileLookup(ModelLookup):
    model = UserProfile
    search_fields = ('firstName__icontains', 'lastName__icontains')
    
registry.register(UserProfileLookup)