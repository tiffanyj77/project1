# Generated by Django 5.0 on 2025-02-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_securityquestion_id_alter_securityquestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityquestion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
