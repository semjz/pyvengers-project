# Generated by Django 4.2.6 on 2023-11-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_alter_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10),
        ),
    ]