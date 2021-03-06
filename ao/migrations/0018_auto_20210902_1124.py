# Generated by Django 3.2.6 on 2021-09-02 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ao', '0017_auto_20210831_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soformodel',
            name='sofor_resim',
        ),
        migrations.RemoveField(
            model_name='soformodel',
            name='sofor_tel_no',
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='arac_cikis_saati',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='arac_giris_saati',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='arac_ilk_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='arac_son_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='araclar',
            field=models.ManyToManyField(blank=True, null=True, related_name='sofor', to='ao.AracModel'),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='sofor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soforler', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='sofor_adi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='sofor_soyadi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='soformodel',
            name='sofor_tc_kimlik_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
