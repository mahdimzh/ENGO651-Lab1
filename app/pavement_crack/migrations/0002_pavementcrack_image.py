# Generated by Django 4.1.5 on 2023-08-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavement_crack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pavementcrack',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
