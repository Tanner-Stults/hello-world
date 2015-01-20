from django import template
from rango.models import Category
from django.contrib.auth.models import User, Group
from rango.models import UserProfile

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat' : cat}

@register.filter(name='has_group')
def has_group(user):
    try:
        group = user.groups.get()
    except Group.DoesNotExist:
        group = None
    return True if group else False

@register.filter(name='looking_for_group')
def has_group(user):
    try:
        group = user.groups.get()
        user_set = group.user_set.all().count()
    except Group.DoesNotExist:
        group = None
        user_set = 0
    return False if group and user_set > 1 else True

@register.filter(name='full_group')
def full_group(user, arg = None):
    try:
        group = user.groups.get()
        user_set = group.user_set.all().count()
    except Group.DoesNotExist:
            group = None
            user_set = 0
                
    return True if group and user_set >= 4 else False

@register.filter(name='in_group')
def in_group(user, arg):
    try:
        group = user.groups.get()
    except Group.DoesNotExist:
        group = None
    if group:
        inGroup = False
        for users in group.user_set.all():
            if users == arg:
                inGroup = True
        return True if inGroup else False

@register.filter(name='get_group_names')
def get_group_names(user, arg = None):
    names = ''
    group = user.groups.get()
    user_set = group.user_set.all()
    for users in user_set:
        if users != user:
            if arg == users:
                names += 'You, '
            else:
                up = UserProfile.objects.get(user=users)
                names += up.firstName +', '
            num = names[:-2].rfind(',') + 1

    if group.user_set.all().count() > 2:
        return names[:num - 1] + " and" + names[num:-2]
    else:
        return names[0:-2]
    