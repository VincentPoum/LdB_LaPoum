# Generated by Django 2.0.3 on 2018-03-20 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LivreDeBord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A', 'Achat'), ('D', 'Déménagement'), ('W', 'Facture eau'), ('E', 'Facture électricité'), ('E', 'Entretien'), ('T', 'Travaux'), ('F', 'Fournitures')], max_length=1, verbose_name='Type')),
                ('somme', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Montant')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReleveEau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compteur', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Index compteur')),
            ],
        ),
        migrations.CreateModel(
            name='ReleveElec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heures_pleines', models.PositiveIntegerField(verbose_name='Heures Pleines')),
                ('heures_creuses', models.PositiveIntegerField(verbose_name='Heures Creuses')),
            ],
        ),
        migrations.AlterField(
            model_name='evenement',
            name='classe',
            field=models.CharField(choices=[('H', 'Histoire'), ('D', 'Dépense'), ('W', 'Relevé Eau'), ('E', 'Relevé électricité'), ('X', 'Autres')], max_length=1),
        ),
        migrations.AddField(
            model_name='releveelec',
            name='lien_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LivreDeBord.Evenement'),
        ),
        migrations.AddField(
            model_name='releveeau',
            name='lien_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LivreDeBord.Evenement'),
        ),
        migrations.AddField(
            model_name='depense',
            name='lien_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LivreDeBord.Evenement'),
        ),
    ]
