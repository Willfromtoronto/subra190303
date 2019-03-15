from django.urls import include, path
from django.contrib import admin

# URL mapping for the root web application.
urlpatterns = [
 path('greet/', include('greet.urls')),
 path('admin/', admin.site.urls),
]


