from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', DashboardView.as_view(), name='dashboard'),
                  path('qr_code_generate/', QRCodeGeneratorView.as_view(), name='qr_code_generator'),
                  path('qr_codes/', QRCodesView.as_view(), name='qr_codes'),
                  path('qr_codes/<int:qr_code_id>/', QRCodeDetailsView.as_view(), name='qr_details'),
                  path('qr_codes/<int:qr_code_id>/delete/', QRCodeDeleteView.as_view(), name='delete_qr'),
                  path('students/', StudentsView.as_view(), name='students'),
                  path('students/<int:student_id>/delete/', StudentDeleteView.as_view(), name='delete_student'),
                  path('form/', StudentRequestView.as_view(), name='student-request'),
                  path('student-create/', StudentRequestDashboardView.as_view(), name='student-request-dashboard'),
                  path('success/', SuccessView.as_view(), name='success'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
