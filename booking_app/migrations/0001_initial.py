# Generated by Django 4.2.11 on 2024-04-04 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.table')),
            ],
        ),
    ]