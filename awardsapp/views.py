from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from awardsapp.models import Profile, Project, AvgRating, Rating


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
    searched_user = User.objects.filter(id=uid).first()
    projects = Project.objects.filter(creator__id=uid).all()
    profile_info = Profile.objects.filter(user__id=uid).first()
    is_current_user_profile = False
    if uid == request.user.id:
        is_current_user_profile = True
    context = {'title': "A profile", "projects": projects, 'profile_info': profile_info,
               'searched_user': searched_user, 'is_current_user_profile': is_current_user_profile}
    return render(request, 'awardsapp/profile.html', context)


@login_required(login_url='/login')
def review_page(request, pid):
    project = Project.objects.filter(id=pid).first()
    current_user_rating = Rating.objects.filter(reviewer=request.user, project=project)

    if current_user_rating or project.creator == request.user:
        return redirect(f'/projects/{pid}')
    else:
        avg_rating = AvgRating.objects.filter(project__id=pid).first()

        if request.method == 'POST':
            content = request.POST.get('content')
            design = request.POST.get('design')
            usability = request.POST.get('usability')

            new_rating = Rating.objects.create(project=project, design=int(design), content=int(content), usability=int(usability), reviewer=request.user)
            if new_rating:
                all_ratings = Rating.objects.filter(project__id=pid).all()
                designs, contents, usabilities = [rating.design for rating in all_ratings], [rating.content for rating in all_ratings], [rating.usability for rating in all_ratings]
                new_design_avg, new_content_avg, new_usability_avg = get_avg(designs), get_avg(contents), get_avg(usabilities)
                if avg_rating:
                    avg_rating.design = new_design_avg
                    avg_rating.content = new_content_avg
                    avg_rating.usability = new_usability_avg

                    avg_rating.save()
                else:
                    AvgRating.objects.create(project=project, design=int(new_design_avg), content=int(new_content_avg),
                                             usability=int(new_usability_avg))

                return redirect(f'/projects/{pid}')

        context = {'title': "Review page", 'project': project, 'avg_rating': avg_rating}
        return render(request, 'awardsapp/review_page.html', context)


@login_required(login_url='/login')
def new_project(request):
    from .forms import ProjectForm
    if request.method == "POST":
        # We're creating an instance of the form with the data from the post req
        form = ProjectForm(request.POST, request.FILES)
        form.instance.creator = request.user
        if form.is_valid():
            form.save()
            return redirect('/')

    form = ProjectForm()
    context = {'title': "Placeholder", "form": form}
    return render(request, 'awardsapp/new_project.html', context)


def view_project_page(request, pid):
    project = Project.objects.filter(id=pid).first()
    avg_rating = AvgRating.objects.filter(project__id=pid).first()
    all_ratings = Rating.objects.filter(project__id=pid).all()
    context = {'title': "Placeholder", 'project': project, 'avg_rating': avg_rating, 'all_ratings': all_ratings,
               'is_project_view': True}
    return render(request, 'awardsapp/view_project_page.html', context)


@login_required(login_url='/login')
def edit_profile_page(request):
    profile = Profile.objects.filter(user__id=request.user.id).first()

    if request.method == "POST":
        website = request.POST.get('website_field')
        name = request.POST.get('name_field')
        bio = request.POST.get('bio_field')

        if name != request.user.first_name:
            user = User.objects.filter(username=request.user.username).first()
            user.first_name = name
            user.save()

        profile.website = website
        profile.bio = bio
        profile.save()
        return redirect(f'/users/{request.user.id}')

    context = {'title': "Placeholder", 'profile': profile}
    return render(request, 'awardsapp/edit_profile.html', context)


def save_form_and_redirect(form, redirect_destination):
    form.save()
    # We're passing the name, that we created in the urls.py of the app, of the url
    return redirect(str(redirect_destination))


def get_avg(all_ratings):
    return sum(all_ratings)/len(all_ratings)
