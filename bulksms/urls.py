from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('reguser/', views.registeruser, name='registeruser'),
    path('login/', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),

    path('automarksms/', views.automarksms, name='automarksms'),
    path('autofastsms/', views.autofastsms, name='autofastsms'),
    path('winpartsms/', views.winpartsms, name='winpartsms'),
    path('autofasttotal/', views.autofasttotal, name='autofasttotal'),
    path('corpsms/', views.corpsms, name='corpsms'),
    
    path('automarkstat/', views.automarkstat, name='automarkstat'),
    path('autofaststat/', views.autofaststat, name='autofaststat'),
    path('winpartstat/', views.winpartstat, name='winpartstat'),
    path('corpsmsstat/', views.corpsmsstat, name='corpsmsstat'),
    path('autofasttotalstat/', views.autofasttotalstat, name='autofasttotalstat'),

    path('reset_password/',auth_views.PasswordResetView.as_view
        (template_name="bulksms/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view
        (template_name="bulksms/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
        (template_name="bulksms/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view
        (template_name="bulksms/password_reset_done.html"),name="password_reset_complete"),

]

    
