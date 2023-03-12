from django.shortcuts import render
from .models import Student
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSeralizer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class StudentAPI(View):
    def get(self,request, *args , **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSeralizer(stu)
            print("Serializer Data ", serializer.data)
            return JsonResponse(serializer.data , safe= False)
        stu = Student.objects.all()
        serializer = StudentSeralizer(stu , many= True)
        print("All Data Serializer", serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self , request , *args , **kargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSeralizer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "data" : serializer.data,
                "msg" : "data is sucessfully Add"
            }
            return JsonResponse(response_data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    
    def put(self, request, *args , **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSeralizer(stu, data = pythondata , partial= True)
        if serializer.is_valid():
            serializer.save()
            response_data= {
                "data": serializer.data,
                "status": "success",
            }
            return JsonResponse(response_data, safe = False)
        response_data = {
            "data" : serializer.errors,
            "status" : "failed"
        }
        return JsonResponse(response_data, safe=False)
    
    def delete(self, request , *args , **kargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        response_data = {"status": "success", "msg": "Data is Deleted"}
        return JsonResponse(response_data, safe=False)
