from django.urls import path

from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("add_item",views.add_item,name="add_item"),
    path("<str:process>",views.show_process,name="process")
]