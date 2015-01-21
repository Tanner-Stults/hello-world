from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import UpdateView

from rango.models import Category, Page, WorkExperience, Painting, UserProfile, Education
from rango.forms import CategoryForm, PageForm, UserForm, UserLoginForm, UserProfileForm, WorkExperienceForm, EducationForm, AddGroupForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

from datetime import datetime
from django.conf import settings
import os, itertools

from rango.bing_search import run_query

def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by # likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    # Get the number of visits to the site.
    # We use the session.get() function to obtain the visits cookie from the server-side database.
    # If the cookie doesn't exist, we default to zero.

    visits = request.session.get('visits')
    if not visits:
        visits = 0

    # This is a I/O varible to see if we need to update the last_visit_time cookie
    # We need to set this to true if it's been more than a day or if the cookie hasn't been set
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    # update the visits cookie with the new about about visits
    request.session['visits'] = visits

    # add the visits to the context_dict to pass to views
    context_dict['visits'] = visits

    if reset_last_visit_time:
       request.session['last_visit'] = str(datetime.now())

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use
    response = render(request,'rango/nba3000.html', context_dict)

    return response

@login_required
def group(request):
    context_dict = {}

    if request.POST :
        print 'in POST'
        if request.POST.get('create_group'):
            u = User.objects.get(id=request.user.id)

            up = UserProfile.objects.get(user = u)
            if u.groups.all().count() == 0:
                group = Group.objects.create(name=up.firstName)
                u.groups.add(group)
            else:
                group = None
            context_dict['group'] = group
        elif request.POST.get('leave_group'):
            print 'in leave_goup'
            u = User.objects.get(id=request.user.id)
            try:
                group = u.groups.get()
            except Group.DoesNotExist:
                group = None
            if group:
                group.user_set.remove(u)
                if group.user_set.all().count() == 0:
                    Group.objects.filter(id=group.id).delete()
                    print 'group deleted'
                context_dict['group'] = group
        return HttpResponseRedirect("/rango/group/")

    else:
        addForm = AddGroupForm()
        context_dict['addForm'] = addForm
        try:
            u = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            u = None
        if u:
            try:
                up = UserProfile.objects.get(user=u)
            except UserProfile.DoesNotExist:
                up = None
            if up:
                if u.groups.all().count() > 0:
                    group = u.groups.get()
                    users = group.user_set.all()
                    context_dict['users'] = users
                    up = []
                    uwe = []
                    uedu = []
                    for us in users:
                        if us.username != 'AnonymousUser':
                            try:
                                uprofile = UserProfile.objects.get(user=us)
                                up.append(uprofile)
                            except UserProfile.DoesNotExist:
                                uprofile = None
                            we = WorkExperience.objects.filter(user=us).order_by('-endDate', 'startDate')
                            if we:
                                uwe.append(we[0])
                            else:
                                uwe.append(None)
                            edu = Education.objects.filter(user=us).order_by('-endDate', 'startDate')
                            if edu:
                                uedu.append(edu[0])
                            else:
                                uedu.append(None)
    
                    zipped = itertools.izip(users, up, uwe, uedu)
                    zipped2 = itertools.izip(users, up, uwe, uedu)
                    context_dict['udict'] = zipped
                    context_dict['udict2'] = zipped2
                else:
                    group = None
                context_dict['group'] = group
            else:
                return HttpResponseRedirect("/rango/add_profile/")

    return render(request,'rango/group.html', context_dict)

def pubProfile(request, id):
    context_dict = {}


    if request.method == 'GET':
        # If the request was not a POST, display the form to enter details.

        u = User.objects.get(id=id)
        user_profile = UserProfile.objects.get(user=u)
        context_dict['up'] = user_profile

        education = Education.objects.filter(user=u)
        context_dict['edu'] = education

        we = WorkExperience.objects.filter(user=u)
        context_dict['we'] = we

        return render(request, 'rango/pub-profile.html', context_dict)

def about(request):
    if request.session.get('visits'):
        visits = request.session.get('visits')
    else:
        visits = 0
    context_dict = {'visits': visits}
    return render(request, 'rango/about.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category).order_by('-views')

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

            context_dict['result_list'] = result_list
            context_dict['query'] = query

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):

    context_dict = {}
    try:
            cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
            cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['form'] = form
    context_dict['category'] = cat
    context_dict['category_name_slug'] = cat.slug
    context_dict['category_name'] = cat.name

    return render(request, 'rango/add_page.html', context_dict)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})

def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

def track_views(request):

    page_id = None
    url = '/rango/'

    if request.method == 'GET':
        print "is get"
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                print page.views
                page.views = page.views + 1
                print page.views
                page.save()
                url = page.url
            except:
                pass
    return HttpResponseRedirect(url)

def register_profile(request):

# If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_profile_form = UserProfileForm(request.POST, request.FILES)

        # If the two forms are valid...
        if user_profile_form.is_valid():
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = user_profile_form.save(commit=False)
            profile.user = request.user
            user = User.objects.get(username = profile.user)
            user.last_name = request.POST['lastName']
            user.first_name = request.POST['firstName']
            user.save()
            print profile.user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if request.FILES.get('picture'):
                print 'picture'
                #profile.picture = request.FILES['picture']

                if request.POST['coords']:
                    print request.POST['coords']
                    crop_profile(request.POST['coords'], request.FILES['picture'], request.FILES['picture'].name, profile)

            if 'bgpicture' in request.FILES:
                profile.bgpicture = request.FILES['bgpicture']

            # Now we save the UserProfile model instance.
            profile.save()

            return HttpResponseRedirect('/rango/profile/')
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_profile_form.errors

            return render(request,
                'rango/profile_registration.html',
                {'user_profile_form': user_profile_form} )
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_profile_form = UserProfileForm()

        # Render the template depending on the context.
        return render(request,
                'rango/profile_registration.html',
                {'user_profile_form': user_profile_form} )

def crop_profile(coords, img, name, profile):
    box = []
    boxStr = coords
    print "in crop_profile"
    num = 0
    for x in range(0, 4):
        if x != 4:
            box.append(int(float(boxStr[num:boxStr.find(" ", num)])))
        else:
            box.append(int(float(boxStr[num:])))
        num = boxStr.find(" ", num)+1

    from PIL import Image
    from django.core.files.base import ContentFile
    from cStringIO import StringIO
    im = Image.open(img)
    (width, height) = im.size

    if abs(box[2]-box[0]) > 300:
        x = (250./abs(box[2]-box[0]))
        y = (300./abs(box[3]-box[1]))
        print x, y
        box[0] = int(box[0]*x)
        box[1] = int(box[1]*y)
        box[2] = int(box[2]*x)
        box[3] = int(box[3]*y)

        im.thumbnail((int(x*width), int(y*height)), Image.ANTIALIAS);

    resized = im.crop(box)
    try:
        f = StringIO()
        resized.save(f, format = 'PNG', optimize = True)
        s = f.getvalue()
        if name :  #TO-DO
            profile.picture.save(name, ContentFile(s))

    finally:
        f.seek(0)
        f.close()

@login_required
def profile(request):
    print 'in profile'
    context_dict = {}

    if request.method == 'GET':
        # If the request was not a POST, display the form to enter details.
        form = WorkExperienceForm()
        context_dict['form'] = form

        eduForm = EducationForm()
        context_dict['eduForm'] = eduForm

        u = User.objects.get(username=request.user)
        try:
            up = UserProfile.objects.get(user=u)
        except UserProfile.DoesNotExist:
            up = None
        if up:
            user_profile_form = UserProfileForm(instance = up)
            context_dict['user_profile_form'] = user_profile_form
            education = Education.objects.filter(user=u).order_by('-endDate', 'startDate')
            existingEduForm = []
            for edu in education:
                exEduForm = EducationForm(instance = edu)
                existingEduForm.append(exEduForm)
            zippedEdu = zip(education, existingEduForm)

            we = WorkExperience.objects.filter(user=u).order_by('-endDate', 'startDate')
            existingExpForm = []
            for exp in we:
                expForm = WorkExperienceForm(instance = exp)
                existingExpForm.append(expForm)
            zippedExp = zip(we, existingExpForm)
            context_dict['user'] = u
            context_dict['userprofile'] = up
            context_dict['education'] = education
            context_dict['zippedExp'] = zippedExp
            context_dict['zippedEdu'] = zippedEdu
            return render(request, 'rango/profile.html', context_dict)
        else:
            return HttpResponseRedirect("/rango/add_profile/")

    else:
        if "jobTitle" in request.POST: # Bad way for handling multiple forms, could cause trouble if user input "jobTitle" Fix with other views
            form = WorkExperienceForm(request.POST, request.FILES)

            # Have we been provided with a valid form?
            if form.is_valid():
                workExperience = form.save(commit=False)
                workExperience.user = request.user
                if 'picture' in request.FILES:
                    workExperience.picture = request.FILES['picture']
                # Save the new category to the database.
                workExperience.save()
            else:
            # The supplied form contained errors - just print them to the terminal.
                print form.errors

        elif "schoolType" in request.POST:
            eduForm = EducationForm(request.POST)
            if eduForm.is_valid():
                education = eduForm.save(commit=False)
                education.user = request.user
                # Save the new category to the database.
                education.save()
            else:
                # The supplied form contained errors - just print them to the terminal.
                print eduForm.errors
        elif "coords" in request.POST:
            profile = UserProfileForm(request.POST)
            profileUser = UserProfile.objects.get(user = request.user)
            if profile.is_valid():
                # Save the new category to the database.
                if request.POST.get('picture-clear') != 'on':
                    crop_profile(request.POST['coords'], request.FILES['picture'], request.FILES['picture'].name, profileUser)
                else:
                    print 'on'
                    profileUser.picture = None
                    profileUser.save()
            else:
                # The supplied form contained errors - just print them to the terminal.
                print profile.errors
        update_profile(request.user)
        return HttpResponseRedirect("/rango/profile/#close")

def update_profile(user):
    print "in update_profile"
    up = UserProfile.objects.get(user = user)
    we = WorkExperience.objects.filter(user=user).order_by('-endDate', 'startDate')
    if we:
        up.currentCompany = we[0].company
        up.currentPosition = we[0].jobTitle
        if we.count() > 1:
            up.previousCompany = we[1].company
            up.previousPosition = we[1].jobTitle
        else:
            up.previousCompany = ''
            up.previousPosition = ''
    else:
        up.currentCompany = ''
        up.currentPosition = ''
    edu = Education.objects.filter(user=user).order_by('-endDate', 'startDate')
    if edu:
        up.education = edu[0].school
    else:
        up.education = ''
    up.save()

def paintings(request):
    context_dict = {}
    if request.method == 'GET':
        paintingList = Painting.objects.all()
        length = len(paintingList)

        context_dict['paintingList'] = paintingList
        context_dict['length'] = length

    return render(request, 'rango/paintings.html', context_dict)

def users(request):
    context_dict = {}
    if request.method == 'GET':
        up = []

        u = User.objects.all()
        for us in u:
            x = UserProfile.objects.get(user=u)
            up.append(x)
        length = len(u)

        udict = {'userdict' : u, 'userprofiledict' : up}
        context_dict['udict'] = zip(u, up)
        context_dict['length'] = length

    return render(request, 'rango/users.html', context_dict)

def xpusers(request):

    context_dict = {}
    if request.method == 'GET':
        u = []
        up = []
        uwe = []
        uedu = []
        user = User.objects.all().order_by('last_name', 'first_name')
        op = User.objects.get(username=request.user)
        for us in user:
            if us.username != 'AnonymousUser' and us != op :
                try:
                    uprofile = UserProfile.objects.get(user=us)
                except UserProfile.DoesNotExist:
                    uprofile = None
                if uprofile:
                    u.append(us)
                    up.append(uprofile)
                    we = WorkExperience.objects.filter(user=us).order_by('-endDate', 'startDate')
                    if we:
                        uwe.append(we[0])
                    else:
                        uwe.append(None)
                    edu = Education.objects.filter(user=us).order_by('-endDate', 'startDate')
                    if edu:
                        uedu.append(edu[0])
                    else:
                        uedu.append(None)
        zipped = itertools.izip(u, up, uwe, uedu)
        zipped2 = itertools.izip(u, up, uwe, uedu)
        context_dict['udict'] = zipped
        context_dict['udict2'] = zipped2

    return render(request, 'rango/xpusers.html', context_dict)


@login_required
def like_category(request):
    print "In like_category";
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
           cat_list = cat_list[:max_results]

    return cat_list

def suggest_category(request):
    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    cat_list = get_category_list(8, starts_with)

    return render(request, 'rango/category_list.html', {'cat_list': cat_list })

def auto_add_page(request):
    cat_id = None
    url = None
    title = None
    context_dict = {}
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        url = request.GET['url']
        title = request.GET['title']

        if cat_id:
            category = Category.objects.get(id=int(cat_id))
            p = Page.objects.get_or_create(category=category, title=title, url=url)

            pages = Page.objects.filter(category=category).order_by('-views')

            # Adds our results list to the template context under name pages.
            context_dict['pages'] = pages

    return render(request, 'rango/page_list.html', context_dict)

def delete_workExperience(request, id):
    workExperience_to_delete = get_object_or_404(WorkExperience, id=id)
    workExperience_to_delete.delete()
    user = User.objects.get(username = request.user)
    update_profile(user)
    return HttpResponseRedirect("/rango/profile/")

def delete_education(request, id):
    education_to_delete = get_object_or_404(Education, id=id)
    education_to_delete.delete()
    user = User.objects.get(username = request.user)
    update_profile(user)
    return HttpResponseRedirect("/rango/profile/")

def save_workExperience(request, id):
    workExperience_to_save = WorkExperience.objects.get(id=id)
   
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, request.FILES, instance=workExperience_to_save)

        if form.is_valid(): # checks CSRF
            workExperience = form.save(commit = False)
            for filename, file in request.FILES.iteritems():
                name = request.FILES[filename].name
                print len(request.FILES)
            print len(request.FILES)
            if 'picture' in request.FILES:
                print "hi"
                workExperience.picture = request.FILES['picture']
            workExperience.save()
        user = User.objects.get(username = request.user)
        update_profile(user)
    return HttpResponseRedirect("/rango/profile/")

def save_education(request, id):
    education_to_save = Education.objects.get(id=id)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = EducationForm(request.POST or None, instance=education_to_save)
        if form.is_valid(): # checks CSRF
            form.save()
        user = User.objects.get(username = request.user)
        update_profile(user)
    return HttpResponseRedirect("/rango/profile/")

def send_email(request, id):
    from django.core.mail import send_mail
    print 'sending...'
    if request.method == 'GET':
        print 'in post...'
        u = User.objects.get(id=request.user.id)
        u2 = User.objects.get(id=id)
        up = UserProfile.objects.get(user = u)

        url = request.build_absolute_uri()
        url = url[:url.rfind('/', 0, (url.rfind('/', 0, -1)))]
        url = url+'/accept_invite/'+str(u2.id)+'?ou='+str(u.id)
        print url
        print u.email
        print u2.email
        send_mail(up.firstName+' has invited you to join their group', up.firstName+' has invited you to join their group. Click here to accept the invite: '+url+'.' , u.email, [u2.email], fail_silently=False)

    return HttpResponseRedirect("/rango/users/")

@login_required
def accept_invite(request, id):
    print 'in accept'
    context_dict = {}
    if request.method == 'GET':
        cu = User.objects.get(id=request.user.id)
        u = User.objects.get(id=id)
        ouId = request.GET.get('ou')
        context_dict['u'] = u
        if u.is_authenticated() and cu == u:
            context_dict['ouId'] = ouId
            if ouId != None:
                ou = User.objects.get(id=ouId)
                oup = UserProfile.objects.get(user=ou)
                context_dict['oup'] = oup
            else:
                return HttpResponseRedirect("/rango/no_user/")
            try:
                group = ou.groups.get()
            except Group.DoesNotExist:
                group = None
            context_dict['group'] = group
            if group:
                u = []
                up = []
                uwe = []
                uedu = []
                for us in group.user_set.all():
                    try:
                        uprofile = UserProfile.objects.get(user=us)
                    except UserProfile.DoesNotExist:
                        uprofile = None
                    if uprofile:
                        u.append(us)
                        up.append(uprofile)
                        we = WorkExperience.objects.filter(user=us).order_by('-endDate', 'startDate')
                        if we:
                            uwe.append(we[0])
                        else:
                            uwe.append(None)
                        edu = Education.objects.filter(user=us).order_by('-endDate', 'startDate')
                        if edu:
                            uedu.append(edu[0])
                        else:
                            uedu.append(None)
                zipped = itertools.izip(u, up, uwe, uedu)
                zipped2 = itertools.izip(u, up, uwe, uedu)
                context_dict['udict'] = zipped
                context_dict['udict2'] = zipped2
                return render(request, 'rango/join_group.html', context_dict)
            else:
                return render(request, 'rango/join_group.html', context_dict)
        else:
            print ' redirecting to '+ '/rango/user_login/?next='+request.path+'?ou='+ouId
            return HttpResponseRedirect('/rango/user_login/?next='+request.path+'?ou='+ouId)
        print "authentication failed"
    else:
        print "in post"
        ouId = request.GET.get('ou')
        if request.POST.get('leave_group'):
            print 'in leave_goup'
            u = User.objects.get(id=id)
            try:
                group = u.groups.get()
            except Group.DoesNotExist:
                group = None
            if group:
                group.user_set.remove(u)
                if group.user_set.all().count():
                    Group.objects.filter(id=group.id).delete()
                    print 'group deleted'
                context_dict['group'] = group
            return HttpResponseRedirect('/rango/accept_invite/'+str(id)+'/?ou='+str(ouId))
        elif request.POST.get('join_group'):
            print 'in join_goup'
            ou = User.objects.get(id=ouId)
            u = User.objects.get(id=id)
            try:
                group = ou.groups.get()
            except Group.DoesNotExist:
                group = None
            if group:
                group.user_set.add(u)
                try:
                    up = UserProfile.objects.get(user=u)
                except UserProfile.DoesNotExist:
                    up = None
                if up:
                    group.name = group.name + ', ' + up.firstName
                    group.save()
                context_dict['group'] = group
            return HttpResponseRedirect('/rango/group/')

def no_user(request):
    if request.method == 'GET':
        return HttpResponseRedirect("/rango/no_user/")

def user_login(request):
    print 'in user_login'
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        if request.GET.get('next', False):
            nextUrl = request.GET['next']
            print nextUrl
        else:
            nextUrl = "/rango/profile/"
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(nextUrl)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your XPJobs account is disabled.")
        else:
            context_dict = {}
            login_form = UserLoginForm(request.POST)
            context_dict['login_form'] = login_form
            context_dict['failed'] = True
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'registration/login.html', context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        context_dict = {}
        login_form = UserLoginForm();
        context_dict['login_form'] = login_form
        if request.GET.get('next', False):
            print 'got next'
            redirect = request.GET['next']
           
            try:
                userIdNum = int(redirect[:-1].rfind("/"))
                userIdNum2 = int(redirect[:userIdNum].rfind("/")) + 1
                userId = redirect[userIdNum2:userIdNum]
                user = User.objects.get(id=userId)
                userProfile = UserProfile.objects.get(user=user)
                context_dict['up'] = userProfile
                context_dict['redirect'] = redirect
            except:
                pass
            print redirect
        return render(request, 'registration/login.html', context_dict)

def ajax_user_search(request):
    from django.template.loader import render_to_string
    print "in function!"
    context_dict = {}
    print "in ajax!"
    q = request.GET.get('q')
    if q is not None:
        print q
        import urllib
        q = urllib.unquote(q)
        from django.db.models import Q
        if q.find(" ") != -1:

            print 'in contains'
            qFirst = q[:q.find(" ")]
            qSecond = q[q.find(" ")+1:]
            results = UserProfile.objects.filter(
                firstName__icontains = qFirst, lastName__icontains = qSecond).order_by('lastName')
        else:
            print 'does not contain'
            print 'this is q: ' + q
            results = UserProfile.objects.filter(
                Q(firstName__icontains = q) |
                Q(lastName__icontains = q)).order_by('lastName')
    ups = []
    us = []
    for user in results:
        ups.append(user)
        us.append(User.objects.get(username=user.user))

    zipped = itertools.izip(us, ups)
    zipped2 = itertools.izip(us, ups)
    try:
        ou = User.objects.get(id = request.user.id)
    except User.DoesNotExist:
        ou = None
    context_dict['ou'] = ou
    context_dict['zipped'] = zipped
    context_dict['zipped2'] = zipped2
    print 'q: ' + q
    context_dict['length'] = results.count()
    return_str = render_to_string( 'rango/results.html', context_dict)
    return HttpResponse(return_str)
