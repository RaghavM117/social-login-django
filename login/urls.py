
from django.contrib import admin
from django.urls import path,include
from social import views as social_views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',social_views.HomeView.as_view(),name='home'),
    
    #login and logout
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    
    path('oauth/',include('social_django.urls',namespace='social')),
    
    path('settings/',social_views.SettingsView.as_view(),name='settings'),
    path('settings/password/',social_views.password, name='password'),
]
