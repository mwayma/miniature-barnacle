# Generated by Django 4.2.4 on 2023-08-12 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='firmware',
            old_name='device_name',
            new_name='branch_name',
        ),
        migrations.RemoveField(
            model_name='firmware',
            name='description',
        ),
        migrations.AddField(
            model_name='firmware',
            name='version',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firmware',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.devicemodel'),
            preserve_default=False,
        ),
    ]
