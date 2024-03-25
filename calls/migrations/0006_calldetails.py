# Generated by Django 5.0.3 on 2024-03-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0005_product_country_product_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=50)),
                ('call_date', models.DateTimeField(null=True)),
                ('call_type', models.CharField(max_length=100)),
                ('transcript', models.TextField(max_length=10000)),
                ('subject_line', models.TextField(max_length=1000)),
                ('aht', models.TextField(max_length=100)),
                ('summary', models.TextField(max_length=10000)),
            ],
        ),
    ]