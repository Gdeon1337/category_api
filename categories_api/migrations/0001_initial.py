# Generated by Django 3.0.2 on 2020-01-16 10:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories_api.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('priority', models.IntegerField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories_api.Attributes')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories_api.Products')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories_api.Attributes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories_api.Categories')),
            ],
        ),
    ]
