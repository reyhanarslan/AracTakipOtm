# Generated by Django 3.2.6 on 2021-08-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ao', '0015_aracmodel_arac'),
    ]

    operations = [
        migrations.AddField(
            model_name='soformodel',
            name='arac_ilk_km',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='soformodel',
            name='arac_son_km',
            field=models.FloatField(null=True),
        ),
    ]
