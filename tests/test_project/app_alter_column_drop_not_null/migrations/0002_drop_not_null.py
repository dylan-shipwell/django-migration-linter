# Generated by Django 2.1.4 on 2019-03-19 21:05

from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app_alter_column_drop_not_null", "0001_create_table")]

    operations = [
        migrations.AlterField(
            model_name="a", name="not_null_field", field=models.IntegerField(null=True)
        )
    ]
