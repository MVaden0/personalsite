from typing import Tuple

from django.contrib import admin
from django.urls import path, include


# site-wide url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
