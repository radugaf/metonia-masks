# Generated by Django 2.2.14 on 2020-11-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201125_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_privacy', models.CharField(max_length=250)),
                ('content_privacy', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refunds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_refunds', models.CharField(max_length=250)),
                ('content_refunds', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_terms', models.CharField(max_length=250)),
                ('content_terms', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'Special Offer'), ('S', 'Limited Edition'), ('D', 'New Collection'), ('N', 'Sold Out')], max_length=1, null=True),
        ),
    ]
