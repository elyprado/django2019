# Generated by Django 2.0.13 on 2019-08-20 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Fornecedor'),
            preserve_default=False,
        ),
    ]
