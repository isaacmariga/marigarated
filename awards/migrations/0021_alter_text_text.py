# Generated by Django 4.0.2 on 2022-07-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0020_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
