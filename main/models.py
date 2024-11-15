from django.db import models


class QRCode(models.Model):
    url = models.URLField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.url)


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
