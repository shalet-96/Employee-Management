# Generated by Django 3.2.9 on 2022-01-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0002_claimmanagement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanagement',
            name='submitted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]