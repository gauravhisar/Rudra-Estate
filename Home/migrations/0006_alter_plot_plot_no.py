# Generated by Django 3.2.3 on 2021-05-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='plot_no',
            field=models.TextField(null=True, unique=True),
        ),
    ]
