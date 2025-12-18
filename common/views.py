from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ExamCreateSerializers, GuruhSerializers, KursSerializer, ExamEnterSerializers
from .models import Exam, Guruh, Kurs
from rest_framework import status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Kurs


class ExamCreateView(APIView):
    permission_classes = [permissions.AllowAny,]
    @swagger_auto_schema(request_body=ExamCreateSerializers)
    
    def post(self, request):
        exam = ExamCreateSerializers(data=request.data)
        
        if exam.is_valid():
            exam.save()
            return Response("Saqlandi!! ", status=status.HTTP_201_CREATED)
        else:
            return Response(exam.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class GuruhListView(APIView):
    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(responses={200: GuruhSerializers(many=True)})
    def get(self, request):
        exams = Guruh.objects.all()
        serializer = GuruhSerializers(exams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class KursListView(APIView):
    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(responses={200: KursSerializer(many=True)})
    def get(self, request):
        kurslar = Kurs.objects.all()
        serializer = KursSerializer(kurslar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ExamEnterView(APIView):
    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(request_body=ExamEnterSerializers)
    def post(self, request):
        exam = ExamEnterSerializers(data=request.data)
        
        if exam.is_valid():
            code = exam.validated_data['code']
            try:
                exam_instance = Exam.objects.get(code=code)
                return Response("Exam topildi!", status=status.HTTP_200_OK)
            except Exam.DoesNotExist:
                return Response("Exam kodi noto'g'ri", status=status.HTTP_404_NOT_FOUND)    
        else:
            return Response(exam.errors, status=status.HTTP_400_BAD_REQUEST)