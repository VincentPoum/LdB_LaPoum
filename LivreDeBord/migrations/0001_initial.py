# Generated by Django 2.0.3 on 2018-03-20 14:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('date_event', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('classe', models.CharField(choices=[('H', 'Histoire'), ('D', 'Dépense'), ('C', 'Charges'), ('X', 'Autres')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Histoire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('lien_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LivreDeBord.Evenement')),
            ],
        ),
    ]
