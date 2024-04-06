from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login,  name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('farmers/', include('farmers.urls')),
    path('register-new-farmer/', views.register_new_farmer, name='register-new-farmer'),
]
