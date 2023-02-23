# Generated by Django 4.1.3 on 2023-02-17 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="buildingattributeinformationmodel",
            name="building",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="utils.planetosmpolygon",
            ),
        ),
    ]