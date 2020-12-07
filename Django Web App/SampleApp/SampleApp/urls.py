from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")), #include all Urls of helo app
    path('mybirthday/', include("mybirthday.urls")), #include all Urls of helo app
    path('tasks/', include("tasks.urls"))
]
