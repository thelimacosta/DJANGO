from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/forum/', permanent=False), name='home'),
    path('hello/', include("hello.urls")),
    path('forum/', include('forum.urls')),
]