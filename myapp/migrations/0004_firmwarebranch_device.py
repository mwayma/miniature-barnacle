# Generated by Django 4.2.4 on 2023-08-12 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_firmwarebranch_remove_firmware_branch_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmwarebranch',
            name='device',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='myapp.devicemodel'),
            preserve_default=False,
        ),
    ]
