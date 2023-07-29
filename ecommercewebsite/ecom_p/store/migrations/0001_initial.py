# Generated by Django 4.2.3 on 2023-07-29 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='images')),
                ('description', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('orginal_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=trending')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]