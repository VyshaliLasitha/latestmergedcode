# Generated by Django 4.0.5 on 2022-06-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_rename_phone_noo_services_account_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='i_Agree',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='email_ID',
            field=models.EmailField(max_length=20),
        ),
    ]
