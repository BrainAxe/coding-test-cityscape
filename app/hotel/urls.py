from django.urls import path, include
# from .views import home_page


urlpatterns = [
    # path('', home_page),
    path('api/', include('hotel.api.urls')),
]