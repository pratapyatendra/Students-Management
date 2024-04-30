# from django.shortcuts import render

# Create your views here.

from rest_framework import APIView
from .serializers import StudentSerializer
from django.http.response import JsonResponse


class StudentsView(APIView):

    def post(self, request):
        data = request.data
        serialzer=StudentSerializer(data=data)

        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)
