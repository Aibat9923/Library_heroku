# Generated by Django 3.1.2 on 2020-12-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201214_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='suit',
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rating',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=1),
        ),
    ]
