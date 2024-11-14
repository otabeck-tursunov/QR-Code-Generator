from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QRCodeGeneratorView.as_view(), name='qr_code_generator'),
    path('qr_codes/', QRCodesView.as_view(), name='qr_codes'),
    path('qr_codes/<int:qr_code_id>/', QRCodeDetailsView.as_view()),
    path('students/', StudentsView.as_view(), name='students'),
    path('form/', StudentRequestView.as_view(), name='student-request'),
    path('success/', SuccessView.as_view(), name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
