from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('profile/<str:username>', views.profile, name='profile'),
    path('create_team', views.create_team, name='create_team'),
    path('search', views.search, name='search'),
    path('create_task/<str:team_name>', views.create_task, name='create_task'),
    path('edit_members/<str:team_name>', views.edit_members, name='edit_members'),
    path('friend_request/<str:username>', views.friend_request, name='friend_request'),
    path('decline_friend_request/<str:username>', views.decline_friend_request, name='decline_friend_request'),
    path('remove_friend_request/<str:username>', views.remove_friend_request, name='remove_friend_request'),
    path('accept_friend_request/<str:username>', views.accept_friend_request, name='accept_friend_request'),
    path('accept_friend_request_from_requests/<str:username>', views.accept_friend_request_from_requests, name='accept_friend_request_from_requests'),
    path('remove_friend/<str:username>', views.remove_friend, name='remove_friend'),
    path('edit_profile/<str:feature_changed>', views.edit_profile, name='edit_profile'),

]