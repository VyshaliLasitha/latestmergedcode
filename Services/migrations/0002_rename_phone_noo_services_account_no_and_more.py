# Generated by Django 4.0.5 on 2022-06-10 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='phone_noo',
            new_name='account_No',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='emailid',
            new_name='email_ID',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='fullname',
            new_name='full_Name',
        ),
        migrations.AddField(
            model_name='services',
            name='address',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='amount',
            field=models.CharField(choices=[('5000', '5000'), ('10000', '10000'), ('15000', '15000'), ('20000', '20000')], default=5000, max_length=30),
        ),
        migrations.AddField(
            model_name='services',
            name='mobile_No',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='services_Types',
            field=models.CharField(choices=[('Cash Pickup', 'Cash Pickup'), ('Cash Delivery', 'Cash Delivery')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]