from django.contrib import admin
from common import models
@admin.register(models.Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    
@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = "id", "code", "kurs", "guruh", "expire_date"
    
    
@admin.register(models.Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = "id", "telegram_id", "name"