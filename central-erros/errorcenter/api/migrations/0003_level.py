# Generated by Django 2.2.4 on 2019-10-22 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(choices=[('DEBUG', 'DEBUG'), ('ERROR', 'ERROR'), ('WARNING', 'WARNING')], max_length=500, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Origin'),
        ),
        migrations.AddField(
            model_name='log',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Level'),
        ),
    ]
