# Generated by Django 2.0.13 on 2019-08-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190815_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=18)),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
    ]
