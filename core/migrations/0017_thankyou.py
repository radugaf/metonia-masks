# Generated by Django 2.2.14 on 2020-12-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20201218_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThankYou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
