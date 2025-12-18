import random
from rest_framework import serializers 
from .models import Kurs, Exam, Guruh



class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = ["id", "name"]
        
class GuruhSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = ["id", "telegram_id", "name"]
        
        
class ExamCreateSerializers(serializers.ModelSerializer):
    code = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Exam
        fields = ["code", "kurs", "guruh", "expire_date"]

    def create(self, validated_data):
        validated_data['code'] = random.randint(1000, 9999)
        return super().create(validated_data)
    
class ExamEnterSerializers(serializers.ModelSerializer):
    code = serializers.IntegerField(max_value=9999, min_value=1000)
    class Meta:
        model = Exam
        fields = ["code"]