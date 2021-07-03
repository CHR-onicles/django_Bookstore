from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('<int:id>/review', views.review, name='review'),
    path('<str:author>', views.author, name='author_books'),
]
