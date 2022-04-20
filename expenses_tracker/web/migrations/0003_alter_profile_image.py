# Generated by Django 4.0.4 on 2022-04-20 11:00

from django.db import migrations, models
import expenses_tracker.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/static/image/user.png', null=True, upload_to='profiles/', validators=[expenses_tracker.web.validators.MaxFileSizeInMbValidator(5)]),
        ),
    ]
