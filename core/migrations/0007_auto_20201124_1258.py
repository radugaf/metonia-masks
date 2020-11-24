# Generated by Django 2.2.14 on 2020-11-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_fata',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_interior',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_lateral2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_laterl1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'Special Offer'), ('S', 'Limited Edition'), ('D', 'New Collection')], max_length=1),
        ),
    ]
