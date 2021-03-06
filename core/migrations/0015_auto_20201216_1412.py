# Generated by Django 2.2.14 on 2020-12-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_sellwithustwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellwithustwo',
            name='image_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sellwithustwo',
            name='image_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sellwithustwo',
            name='image_4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sellwithustwo',
            name='image_5',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='terms',
            name='comanda',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='conformitatea_produselor',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='contul',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='definitii',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='dispozitii_generale',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='dreptu_denuntare',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='facturare_plata',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='gdpr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='informatiile_prezentate',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='livrarea',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='politica_de_vanzare',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='promovare_produse_si_oferte',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='proprietate_intelectuala',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='raspundere',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='reguli_de_utilizare',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='sesizari',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='transferul_proprietatii',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='ultima_legislatie',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='privacy',
            name='content_privacy',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='refunds',
            name='content_refunds',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sellwithustwo',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='terms',
            name='content_terms',
            field=models.TextField(null=True),
        ),
    ]
