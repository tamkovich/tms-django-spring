# Generated by Django 3.2.6 on 2021-08-14 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('style', models.CharField(max_length=50)),
                ('albums', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discs.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discs.track'),
        ),
    ]
