# Generated by Django 3.2.7 on 2021-09-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='text',
            field=models.TextField(default=''),
        ),
    ]