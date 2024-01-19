from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many = True)
    return Response({'status' : 200 , 'payload' : serializer.data})

@api_view(['POST'])
def post_data(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        return Response({'status' : 403 ,  'messege' : 'Something went wrong please check'})
    serializer.save()

    return Response({'status' : 200 , 'payload' : serializer.data, 'messege' : 'you sent'})

def index(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        fage = request.POST.get("age")
        fdesignation = request.POST.get("designation")
        form = Teacher(name = fname,age = fage,designation = fdesignation)
        form.save()
    return render(request,'index.html')