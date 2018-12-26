# Generated by Django 2.1 on 2018-09-16 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='M1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kode', models.CharField(max_length=255)),
                ('cookie', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='m1',
            name='usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontpage.User'),
        ),
    ]