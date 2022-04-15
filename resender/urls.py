from resender.views import GetIdApiView
from django.urls import path, include

urlpatterns = [
    path('get-id/', GetIdApiView.as_view(), name='get-id/'),
]