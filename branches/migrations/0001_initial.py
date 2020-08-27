# Generated by Django 3.1 on 2020-08-27 15:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commercial_name', models.CharField(max_length=255)),
                ('legal_name', models.CharField(max_length=255)),
                ('tax_regime', models.CharField(max_length=255, null=True)),
                ('tax_id', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
