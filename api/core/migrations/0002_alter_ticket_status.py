# Generated by Django 4.0.4 on 2022-04-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[('1', 'resolved'), ('2', 'unresolved'), ('3', 'frozen')], default=2, verbose_name='status of ticket'),
        ),
    ]