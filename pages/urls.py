from django.urls import path
from .views import PdfView


urlpatterns = [
    path('', PdfView, name='pdfs')

]