# Generated by Django 5.1.3 on 2024-11-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='created',
            new_name='created_at',
        ),
    ]