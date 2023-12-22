# Generated by Django 4.2.6 on 2023-10-25 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('extract', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-update_time'],
            },
        ),
    ]