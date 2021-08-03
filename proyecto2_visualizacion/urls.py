from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('time_display.urls')),
    path('admin/', admin.site.urls),
    path('random_word/', include('random_word.urls')),
]
