# Generated by Django 3.2.12 on 2022-04-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_casestudy'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='sub_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Sub Title'),
        ),
    ]