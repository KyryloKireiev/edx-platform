from django.urls import path
from lms.djangoapps.onboarding import views

app_name = 'lms.djangoapps.onboarding'

urlpatterns = [
    path('', views.get_onboarding_page, name='onboarding_page'),
]
