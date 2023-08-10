from django.shortcuts import render
from rest_framework import views
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.

class TestAPIView(views.APIView):
    serializer_class = TestSerializer

    def get(self, request):
        latest_ = Test.objects.latest("id")
        print(latest_)
        serializer = self.serializer_class(latest_)
        return Response(serializer.data)

