import random
from rest_framework import serializers 
from .models import Kurs, Exam, Guruh, Savol



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
        
        
class SavolSerializer(serializers.ModelSerializer):
    
    # kurs = KursSerializer(many=True)
    
    class Meta:
        model = Savol
        fields = ["id", "kurs" , "matn",  "variant_a", "variant_b", "variant_c", "variant_d", "javob"]
        
    def create(self, validated_data):
        kurs_data = validated_data.pop('kurs')
        savol = Savol.objects.create(**validated_data)
        savol.kurs.set(kurs_data)
        return savol