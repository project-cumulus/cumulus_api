# Generated by Django 4.2.5 on 2023-10-16 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_transaction_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('currency', models.CharField(blank=True, max_length=3)),
                ('time_zone', models.CharField(max_length=50)),
                ('last_refreshed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SecPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.DecimalField(decimal_places=4, max_digits=20)),
                ('high', models.DecimalField(decimal_places=4, max_digits=20)),
                ('low', models.DecimalField(decimal_places=4, max_digits=20)),
                ('close', models.DecimalField(decimal_places=4, max_digits=20)),
                ('volume', models.IntegerField()),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='security_price_history', to='api.security')),
            ],
        ),
    ]
