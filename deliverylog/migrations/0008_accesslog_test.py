# Generated by Django 3.2.16 on 2022-11-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverylog', '0007_alter_accesslog_time_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslog',
            name='test',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
