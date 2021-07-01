from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('book/<int:id>', views.detail, name='detail'),
    path('<int:id>/review', views.review, name='review')
]
