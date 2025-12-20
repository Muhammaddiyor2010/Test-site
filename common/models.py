from django.db import models
import uuid
from django.utils import timezone

from datetime import timedelta
import random


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Kurs(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    first_name = models.CharField(
        max_length=20, verbose_name="Ism", null=False, blank=False
    )
    last_name = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="Familiya"
    )
    exam = models.ForeignKey("Exam", on_delete=models.CASCADE, related_name="students")


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
    kurs = models.ManyToManyField("Kurs", related_name="kurslar")
    matn = models.TextField()
    variant_a = models.CharField()
    variant_b = models.CharField()
    variant_c = models.CharField()
    variant_d = models.CharField()
    javob = models.CharField(choices=options)


class Guruh(models.Model):
    telegram_id = models.CharField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Exam(Base):
    code = models.IntegerField(unique=True, verbose_name="Exam Code", blank=True, null=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name="exams")
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    Natija = models.ForeignKey(Natija, on_delete=models.CASCADE, null=True, blank=True)
    expire_date = models.DateField(default=timezone.now() + timedelta(days=1), verbose_name="Expire Date", blank=True)

    