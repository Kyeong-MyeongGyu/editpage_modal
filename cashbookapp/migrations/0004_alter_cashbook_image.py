# Generated by Django 4.0.4 on 2022-09-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0003_cashbook_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
