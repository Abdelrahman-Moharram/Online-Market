# Generated by Django 4.2.1 on 2023-05-12 08:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import home.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productUUID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.TextField(verbose_name='Product Category')),
                ('ar_title', models.TextField(verbose_name='اسم المنتج')),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=5)),
                ('ar_description', models.TextField(blank=True, null=True)),
                ('discount', models.FloatField()),
                ('stock', models.IntegerField(default=1)),
                ('favourite', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Product Category')),
                ('ar_title', models.CharField(max_length=40, verbose_name='نوع المنتج')),
                ('Category_image', models.ImageField(upload_to=home.models.ProductCategory.imagesave)),
            ],
        ),
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=40)),
                ('value', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=home.models.ProductImage.imagesave)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='shop_employee',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='shop_employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shopowner',
            name='user',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='Shop_Employee',
        ),
        migrations.DeleteModel(
            name='ShopOwner',
        ),
        migrations.AddField(
            model_name='product',
            name='productCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.shop_employee'),
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.shop'),
        ),
    ]
