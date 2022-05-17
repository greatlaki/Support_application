# Generated by Django 4.0.4 on 2022-04-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=2, verbose_name='status of ticket'),
        ),
    ]
