# Generated by Django 3.1.3 on 2020-12-21 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20201216_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='characters.character')),
            ],
        ),
    ]
