# Generated by Django 4.0.2 on 2022-04-10 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='uploads/A_products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estore.category')),
            ],
        ),
    ]
