# Generated by Django 3.2.16 on 2022-11-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverylog', '0002_auto_20221106_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='passenger1_first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger1_last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger2_first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger2_last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger3_first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger3_last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger4_first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='passenger4_last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]