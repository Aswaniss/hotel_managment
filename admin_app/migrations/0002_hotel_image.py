# Generated by Django 5.1.3 on 2024-12-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(default='sample_img', upload_to='image'),
        ),
    ]
