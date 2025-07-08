from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def test_view(request):
    return Response({"message": "Hello from listings!"})

urlpatterns = [
    path('test/', test_view, name='test-view'),
]
