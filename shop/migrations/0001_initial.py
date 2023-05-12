# Generated by Django 4.2.1 on 2023-05-12 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('shop_name', models.CharField(max_length=20, unique=True)),
                ('Created_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=40)),
                ('shop_image', models.ImageField(default='users/logo.png', upload_to=shop.models.Shop.imagesave)),
            ],
        ),
        migrations.CreateModel(
            name='ShopOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='shop.shopowner'),
        ),
    ]