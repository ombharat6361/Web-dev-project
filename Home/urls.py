from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('donations/',views.donations,name = 'donations'),
    path('blogadd/',views.blogadd,name='blogadd'),
    path('',views.home, name='home'),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutPage,name="logout"), 
    path("register/",views.registerPage,name="register"),
    path('blogpost/<int:pk>',views.blogpost,name='blogpost'),
    path('about-cancer/',views.aboutcancer,name='aboutcancer'),
    path("delete-room/<int:pk>/",views.DeleteRoom,name="delete-room"),
    path("create-room/",views.createRoom,name="create-room"),
    path("update-room/<int:pk>/",views.UpdateRoom,name="update-room"),
    path('roomforum/',views.roomforum,name='roomforum'),
    path('blogroom/',views.blogroom,name='blogroom'),
    path('room/<int:pk>',views.room,name='room'),
    path("delete-message/<int:pk>/",views.delete_message,name="delete-message"),
    path("profile/<str:pk>",views.userProfile,name="user-profile"), 
    path("search/",views.search, name='search'),
    path("searchroom/",views.searchroom, name='searchroom'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
]