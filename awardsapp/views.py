from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect

from awardsapp.models import Profile, Project


@login_required(login_url='/login')
def logout_method(request):
    logout(request)
    return redirect('/')


def login_page(request):
    auth_req = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('identifier_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            # The authenticate fun below will either return a user obj. tha matches the cred.s we've provides or None
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # The login fun will add a session for the user logging them in
                login(request, user)

                # Once the user has been logged in successfully we wanna redirect them to the home page
                return redirect('/')
            else:
                messages.error(request, "The username and password don't matches")

        except :
            messages.error(request, "The username and password don't match")

    context = {'title': "Login", 'auth_req': auth_req}
    return render(request, 'awardsapp/login_register.html', context)


def register_page(request):
    auth_req = 'register'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('username_field')
        name = request.POST.get('name_field')
        email = request.POST.get('email_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            user = User.objects.get(username=username)

            if user is None:
                new_user = User.objects.create_user(username=username, email=email, password=password)

                Profile.objects.create(user=new_user, bio='', website='')
                # Once the user has been logged in successfully we wanna redirect them to the home page
                print("The creation was successful")
                return redirect('/login')
            else:
                print("The creation was not successful")
                messages.error(request, "The username and password don't matches")

        except :
            new_user = User.objects.create_user(username=username, first_name=name, email=email, password=password)

            Profile.objects.create(user=new_user, bio='', website='')
            # Once the user has been logged in successfully we wanna redirect them to the home page
            print("The creation was successful")
            return redirect('/login')
            # messages.error(request, "The username and password don't match")

    context = {'title': "Register", 'auth_req': auth_req}
    return render(request, 'awardsapp/login_register.html', context)


# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {"title": 'Placeholder', 'is_logged_in': request.user, "projects": projects}
    return render(request, 'awardsapp/index.html', context)


def profile_page(request, uid):
    projects = Project.objects.filter(creator__id=uid).all()
    profile_info = Profile.objects.filter(user__id=uid).first()
    # todo Make a search request for a user with the specified uid
    context = {'title': "A profile", "projects": projects, 'profile_info': profile_info}
    return render(request, 'awardsapp/profile.html', context)


def review_page(request, pid):
    if request.method == 'POST':
        content = request.POST.get('content')
        design = request.POST.get('design')
        usability = request.POST.get('usability')

        print(f'The review Content -{content}, Design -{design}, Usability -{usability}')

    context = {'title': "Review page"}
    return render(request, 'awardsapp/review_page.html', context)


def new_project(request):
    from .forms import ProjectForm
    if request.method == "POST":
        # We're creating an instance of the form with the data from the post req
        form = ProjectForm(request.POST,request.FILES)
        form.instance.creator = request.user
        print(f"The form is {form}")
        if form.is_valid():
            save_form_and_redirect(form, '/')
    form = ProjectForm()
    context = {'title': "Placeholder", "form": form}
    return render(request, 'awardsapp/new_project.html', context)


def view_project_page(request, pid):
    project = Project.objects.filter(id=pid).all()
    context = {'title': "Placeholder", 'project': project, 'is_project_view': True}
    return render(request, 'awardsapp/view_project_page.html', context)


def save_form_and_redirect(form, redirect_destination):
    form.save()
    # We're passing the name, that we created in the urls.py of the app, of the url
    return redirect(str(redirect_destination))

