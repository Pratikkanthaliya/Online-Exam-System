from .views import *
from django.urls import path

urlpatterns = [
    path('new-question/',newQuestion),
    path('save-question/',saveQuestion),
    path('view-questions/',viewQuestions),
    path('edit-question/',editquestion),
    path('edit-save-question/',editsavequestion),
    path('delete-question/',deletequestion),
    path('signup/',signup),
    path('save-user/',saveUser),
    path('login/',login),
    path('login-validation/',loginvalidation),
    path('logout/',logout),
    path('home/',home),
    path('start-test/',startTest),
    path('test-result/',testResult),
]