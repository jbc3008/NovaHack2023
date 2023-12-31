# Generated by Django 4.2.6 on 2023-10-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gafa',
            name='astigmatismo_left',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gafa',
            name='astigmatismo_right',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gafa',
            name='hipermetropia_left',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gafa',
            name='hipermetropia_right',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gafa',
            name='miopia_left',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gafa',
            name='miopia_right',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
