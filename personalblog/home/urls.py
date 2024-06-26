from django.urls import path

from  . import views

urlpatterns = [
    path("home/", views.Homeview, name="home"),
    path("home/view/<int:pk>", views.Detaildisplay, name="post-page"),
    path("home/view/<int:pk>/blog/edit", views.Updateblog.as_view(), name="blog-update"),
    path("home/view/<int:pk>/blog/delete", views.Deleteblog.as_view(), name="blog-delete"),
    path("home/view/new", views.Createblog.as_view(), name ="createblog"),
    
]