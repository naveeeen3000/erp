# Generated by Django 4.1.7 on 2023-03-30 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('pincode', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstituteTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=20)),
                ('school_level', models.CharField(max_length=50)),
                ('from_grades', models.PositiveIntegerField()),
                ('to_grade', models.PositiveBigIntegerField()),
                ('from_age', models.PositiveIntegerField()),
                ('to_age', models.PositiveIntegerField()),
                ('years', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(db_index=True, max_length=20)),
                ('bounds', models.JSONField()),
                ('zone_pincode', models.CharField(db_index=True, max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cities')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
