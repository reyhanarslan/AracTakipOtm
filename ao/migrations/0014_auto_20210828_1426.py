# Generated by Django 3.2.5 on 2021-08-28 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ao', '0013_auto_20210828_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guzergahmodel',
            name='araclar',
            field=models.ManyToManyField(blank=True, null=True, related_name='guzergah', to='ao.AracModel'),
        ),
        migrations.AlterField(
            model_name='guzergahmodel',
            name='guzergah',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guzergahlar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profilmodel',
            name='isim_soyisim',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profilmodel',
            name='kullanici_adi',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profilmodel',
            name='mail',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
    ]
