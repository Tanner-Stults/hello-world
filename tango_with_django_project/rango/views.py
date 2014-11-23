from django.shortcuts import render
from django.shortcuts import HttpResponse

from rango.models import Category
from rango.models import Page

from rango.forms import CategoryForm
from rango.forms import PageForm
from rango.forms import UserForm, UserProfileForm
from rango.forms import UserProfile

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User


from datetime import datetime

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
    response = render(request,'rango/index.html', context_dict)

    return response


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


"""def register(request):
    
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
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
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {})
    

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')
    """

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
        user_profile_form = UserProfileForm(data=request.POST)
        
        # If the two forms are valid...
        if user_profile_form.is_valid():
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = user_profile_form.save(commit=False)
            profile.user = request.user
            print profile.user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_profile_form.errors

        return HttpResponseRedirect('/rango/')
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_profile_form = UserProfileForm()

        # Render the template depending on the context.
        return render(request,
                'rango/profile_registration.html',
                {'user_profile_form': user_profile_form} )

def profile(request):
    context_dict = {}
    if request.method == 'GET':
        
        u = User.objects.get(username=request.user)
        up = UserProfile.objects.get(user=u)

        context_dict['user'] = u
        context_dict['userprofile'] = up
        
    return render(request, 'rango/profile.html', context_dict)


def users(request):
    context_dict = {}
    if request.method == 'GET':
        up = []
        u = User.objects.all()
        for us in u:
            x = UserProfile.objects.get(user=us)
            up.append(x)
        length = len(u)
        
        udict = {'userdict' : u, 'userprofiledict' : up}
        context_dict['udict'] = zip(u, up)
        context_dict['length'] = length
        
    return render(request, 'rango/users.html', context_dict)

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