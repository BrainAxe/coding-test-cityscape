from django.urls import path

from .views import BookRoom


urlpatterns = [

    path('v1/book-room/', BookRoom.as_view(), name='api_book_room'),

]