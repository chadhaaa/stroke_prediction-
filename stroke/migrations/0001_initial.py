# Generated by Django 3.2 on 2021-04-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.FloatField()),
                ('age', models.FloatField()),
                ('hypertension', models.FloatField()),
                ('heart_disease', models.FloatField()),
                ('ever_married', models.FloatField()),
                ('work_type', models.FloatField()),
                ('residence_type', models.FloatField()),
                ('avg_glucose_level', models.FloatField()),
                ('bmi', models.FloatField()),
                ('smoking_status', models.FloatField()),
                ('stroke', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]