# Generated by Django 3.1.5 on 2021-02-18 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'Aboutus', 'verbose_name_plural': 'Aboutus'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'Chef', 'verbose_name_plural': 'Chef'},
        ),
        migrations.AlterModelOptions(
            name='why_choose_us',
            options={'verbose_name': 'Why_Choose_Us', 'verbose_name_plural': 'Why_Choose_Us'},
        ),
    ]
