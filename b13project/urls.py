"""
URL configuration for b13project project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomSignUpView, anonymous_login, login_view

urlpatterns = [
    path("", views.landing_page, name="homepage"),
    path("admin/", admin.site.urls),
    path("accounts/signup/", CustomSignUpView.as_view(), name="account_signup"),
    path("accounts/login/", views.CustomLoginView.as_view(), name="account_login"),
    path('accounts/logout/', views.logout_view, name='account_logout'),
    path("accounts/", include("allauth.urls")),
    path('anonymous-login/', views.anonymous_login, name='anonymous_login'), 
    path('anonymous-project-list/', views.anonymous_project_list, name='anonymous_project_list'),  # Correct path for anonymous login
    path('login/', login_view, name='login'),
    #path('projects/anonymous/', views.anonymous_project_list, name='anonymous_project_list'),
    path("create_profile/", views.create_user_profile, name="create_user_profile"),
    # PMA STUFF 
    path("pma_dashboard/", views.pma_dashboard, name="pma_dashboard"),  # PMA Dashboard
    path('manage_projects/', views.manage_projects, name='manage_projects'),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("login_redirect/", views.login_redirect, name="login_redirect"),
    path('your_projects/', views.your_projects, name='your_projects'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path("view_profile/", views.view_profile, name="view_profile"),
    path('travel-guide/', views.travel_guide, name='travel_guide'),
    #path('view-all-member-projs/', views.view_all_member_projs, name='view_all_member_projs'),
    path('project/vote/', views.vote, name='vote'),
# Add project management URLs
    path('projects/owned/', views.your_projects, name='your_projects'),
    path('projects/joined/', views.joined_projects, name='project_list'),
    #path('projects/', views.project_list, name='project_list'),
    path("projects/<int:project_id>/upload/", views.file_upload, name="project_file_upload"),
    path("projects/create/", views.create_project, name="create_project"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/<int:project_id>/add_member/", views.add_member_to_project, name="add_member"),
    path("projects/<int:project_id>/post_message/", views.post_project_message, name="post_message"),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/request-to-join/', views.request_to_join, name='request_to_join'),
    path('project/<int:project_id>/manage-requests/', views.manage_requests, name='manage_requests'),
    path('project/<int:project_id>/leave/', views.leave_project, name='leave_project'),
    path("explore-projects/", views.explore_projects, name="explore_projects"),



]