# Generated by Django 4.2.6 on 2023-11-24 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('unitselection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyEnrollmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='study_enrollment_files/')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_requests', to='management.faculty')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_requests', to='management.student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_requests', to='management.term')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyCourseDropRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('request_result', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=8)),
                ('student_explanation', models.TextField(blank=True, null=True)),
                ('supervisor_explanation', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_course_drop_request', to='management.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_course_drop_request', to='management.student')),
            ],
        ),
    ]