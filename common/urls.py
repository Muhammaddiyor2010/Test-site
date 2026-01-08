from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ExamCreateView, GuruhListView, KursListView, ExamEnterView, SavolCreate, SavolList, ResultView, RegisterView

urlpatterns = [
    path("exam-create/", ExamCreateView.as_view(), name="exam-create"),
    path("guruh-list/", GuruhListView.as_view(), name="guruh-list"),
    path("kurs-list/", KursListView.as_view(), name="kurs-list"),
    path("exam-enter/", ExamEnterView.as_view(), name="exam-enter"),
    path("savol-list/", SavolList.as_view(), name="savol-list"),
    path("savol-create/", SavolCreate.as_view(), name="savol-create"),
    path("result/", ResultView.as_view(), name="result"),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
