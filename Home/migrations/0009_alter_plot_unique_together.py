# Generated by Django 3.2.3 on 2021-06-03 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20210527_1655'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plot',
            unique_together={('plot_no', 'project')},
        ),
    ]
