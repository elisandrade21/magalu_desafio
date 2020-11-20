# Generated by Django 3.1.3 on 2020-11-18 23:29

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('product_code', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000)])),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('status', models.CharField(choices=[('available', 'Disponível'), ('unavailable', 'Indisponível'), ('deleted', 'Deletado')], default='unavailable', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
