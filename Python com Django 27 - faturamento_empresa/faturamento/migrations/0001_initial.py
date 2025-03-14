# Generated by Django 5.1.2 on 2025-02-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faturamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('janeiro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fevereiro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('abril', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('junho', models.DecimalField(decimal_places=2, max_digits=10)),
                ('julho', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agosto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('setembro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outubro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('novembro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dezembro', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
