from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ExamCreateSerializers, GuruhSerializers, KursSerializer, ExamEnterSerializers, SavolSerializer
from rest_framework import generics
from .models import Exam, Guruh, Kurs, Savol
from rest_framework import status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Kurs
from rest_framework.generics import ListCreateAPIView


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
        
class KursListView(ListCreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [permissions.AllowAny,]
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = KursSerializer(queryset, many=True)
        return Response(serializer.data)

    
class ExamEnterView(APIView):
    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(request_body=ExamEnterSerializers)
    def post(self, request):
        exam = ExamEnterSerializers(data=request.data)
        savollar = SavolSerializer()
        
        if exam.is_valid():
            code = exam.validated_data['code']
            
            try:
                exam_instance = Exam.objects.get(code=code)
                exam = Exam.objects.get(code=code)
                savollar = []
                
                savollar_obj = Savol.objects.filter(kurs = exam.kurs)
                for i in savollar_obj: # type: ignore
                    savol ={}
                    savol["matn"] = i.matn
                    savol["variant_a"] = i.variant_a
                    savol["variant_b"] = i.variant_b
                    savol["variant_c"] = i.variant_c
                    savol["variant_d"] = i.variant_d
                    savollar.append(savol)
                   
                
                return Response({"message": "Exam topildi!", "savollar": savollar}, status=status.HTTP_200_OK)
            except Exam.DoesNotExist:
                return Response("Exam kodi noto'g'ri", status=status.HTTP_404_NOT_FOUND)        
        else:
            return Response(exam.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class SavolList(generics.ListAPIView):
    queryset = Savol.objects.all()
    serializer_class = SavolSerializer
    permission_classes = [permissions.AllowAny,]
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SavolSerializer(queryset, many=True)
        return Response(serializer.data)


class SavolCreate(APIView):
    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(request_body=SavolSerializer)
    
    def post(self, request):
        serializer = SavolSerializer(data=request.data)
        
        
        if serializer.is_valid():
            serializer.save()
            return Response("Savol saqlandi!! ", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)