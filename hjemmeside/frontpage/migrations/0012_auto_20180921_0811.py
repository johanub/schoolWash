# Generated by Django 2.1 on 2018-09-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0011_auto_20180918_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('maskine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontpage.Maskiner')),
            ],
        ),
    ]