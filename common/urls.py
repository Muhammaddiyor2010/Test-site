from django.urls import path

from .views import ExamCreateView, GuruhListView, KursListView, ExamEnterView, SavolCreate, SavolList

urlpatterns = [
    path("exam-create/", ExamCreateView.as_view(), name="exam-create"),
    path("guruh-list/", GuruhListView.as_view(), name="guruh-list"),
    path("kurs-list/", KursListView.as_view(), name="kurs-list"),
    path("exam-enter/", ExamEnterView.as_view(), name="exam-enter"),
    path("savol-list/", SavolList.as_view(), name="savol-list"),
    path("savol-create/", SavolCreate.as_view(), name="savol-create"),
]
