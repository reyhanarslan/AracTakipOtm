# Generated by Django 3.2.5 on 2021-08-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ao', '0010_auto_20210828_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilmodel',
            name='deneme',
        ),
        migrations.AlterField(
            model_name='profilmodel',
            name='araclar',
            field=models.ManyToManyField(blank=True, null=True, related_name='profil', to='ao.AracModel'),
        ),
    ]
