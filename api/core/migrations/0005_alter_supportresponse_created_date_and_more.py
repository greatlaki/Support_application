# Generated by Django 4.0.4 on 2022-04-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportresponse',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
