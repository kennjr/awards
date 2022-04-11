from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_method, name='logout_page'),
    path('users/<int:uid>', views.profile_page, name="profile_page"),
    path('new-project/', views.new_project, name="new_project_page"),
    path('projects/<int:pid>/new-review', views.review_page, name="review_page"),
    path('projects/<int:pid>/', views.view_project_page, name="view_project_page")
]

