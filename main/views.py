from django.http import HttpResponse
from io import BytesIO
import qrcode
from django.core.files import File

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import QRCode, Student


class QRCodesView(View):
    def get(self, request):
        context = {
            'qr_codes': QRCode.objects.all(),
        }
        return render(request, 'qr_codes.html', context)


class QRCodeDetailsView(View):
    def get(self, request, qr_code_id):
        qr_code = get_object_or_404(QRCode, id=qr_code_id)
        context = {
            'qr_code': qr_code
        }
        return render(request, 'qr_code_details.html', context)


class QRCodeGeneratorView(View):
    def get(self, request):
        return render(request, 'qr_code_generator.html')

    def post(self, request):
        qr_code = QRCode.objects.create(
            url=request.POST.get('url'),
        )

        qr_img = qrcode.make(qr_code.url)

        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)
        qr_code.image.save(f'qr_code_{qr_code.id}.png', File(buffer), save=True)

        return redirect(f'/qr_codes/{qr_code.id}/')


class StudentsView(View):
    def get(self, request):
        context = {
            'students': Student.objects.all()
        }
        return render(request, 'students.html', context)


class StudentRequestView(View):
    def get(self, request):
        return render(request, 'request.html')

    def post(self, request):
        Student.objects.create(
            full_name=request.POST.get('full_name'),
            phone_number=request.POST.get('phone_number')
        )
        return redirect('/success/')


class SuccessView(View):
    def get(self, request):
        return HttpResponse('Muvaffaqiyatli! E\'tiboringiz uchun rahmat!')
