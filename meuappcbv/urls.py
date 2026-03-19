from django.urls import path

urlpatterns = [
    path('', views.ViaCepFormView.as_view)
]