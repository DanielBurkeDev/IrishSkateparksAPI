# Generated by Django 4.2.6 on 2023-10-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0002_alter_skateparks_helmets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skateparks',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
