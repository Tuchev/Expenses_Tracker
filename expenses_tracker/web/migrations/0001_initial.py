# Generated by Django 4.0.4 on 2022-04-19 00:08

import django.core.validators
from django.db import migrations, models
import expenses_tracker.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses_tracker.web.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses_tracker.web.validators.validate_only_letters])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[expenses_tracker.web.validators.MaxFileSizeInMbValidator(5)])),
            ],
        ),
    ]
