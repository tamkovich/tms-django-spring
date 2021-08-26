# Generated by Django 3.2.5 on 2021-08-09 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210809_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=50, null=True)),
                ('address', models.CharField(default=None, max_length=50, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='articles.author')),
            ],
        ),
    ]