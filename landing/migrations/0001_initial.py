# Generated by Django 4.0.2 on 2022-02-21 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ALL_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Cybersecurity and IT reviews', 'Cybersecurity and IT reviews'), ('IT Software and Solutions', 'IT Software and Solutions'), ('IT Project consulting', 'IT Project consulting')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('types', models.CharField(blank=True, choices=[('Service', 'Service'), ('Solution', 'Solution')], max_length=255)),
                ('description', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='landing.all_category')),
            ],
        ),
    ]
