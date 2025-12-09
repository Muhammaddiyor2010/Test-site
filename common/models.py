from django.db import models
import uuid



class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")

    created_at = models.DateField(auto_created=True, verbose_name="yaratilgan vaqti")
    updated_at = models.DateField(auto_created=True, verbose_name="yangilangan vaqti")

class Kurs(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    
    

class Student(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Ism", null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False, verbose_name="Familiya")
    exam = models.ForeignKey("Exam", on_delete=models.CASCADE, related_name="students")
    
    
class Exam(Base):
    code =models.IntegerField(verbose_name="Imtihon kodi", unique=True)
    kurs = models.ForeignKey("Kurs", on_delete=models.CASCADE)
    guruh = models.ForeignKey("Guruh", on_delete=models.CASCADE)
    
    natija = models.ForeignKey("Natija", on_delete=models.CASCADE)
    expire_date = models.DateTimeField(verbose_name="Imtihon tugash vaqti")
    
class Natija(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    savol = models.ForeignKey("Savol", on_delete=models.CASCADE)
    javob = models.CharField()
    

class Savol(models.Model):
    options = (
        ("variant_a", "variant_a"),
        ("variant_b", "variant_b"),
        ("variant_c", "variant_c"),
        ("variant_d", "variant_d"),
    )
    kurs = models.ForeignKey("Kurs", on_delete=models.CASCADE)
    matn = models.TextField()
    variant_a = models.CharField()
    variant_b = models.CharField()
    variant_c = models.CharField()
    variant_d = models.CharField()
    javob = models.CharField(choices=options)
    
class Guruh(models.Model):
    telegram_id = models.CharField()
    name = models.CharField(max_length=50)