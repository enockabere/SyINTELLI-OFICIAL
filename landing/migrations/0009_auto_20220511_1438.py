# Generated by Django 3.2.12 on 2022-05-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_remove_testimonial_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partners',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]