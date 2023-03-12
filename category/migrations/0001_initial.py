# Generated by Django 4.1.7 on 2023-03-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15, verbose_name='Time')),
                ('Date', models.CharField(db_index=True, default='nakia', max_length=15, verbose_name='Place')),
            ],
        ),
    ]
