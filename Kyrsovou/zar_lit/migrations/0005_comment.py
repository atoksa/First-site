# Generated by Django 4.0.5 on 2022-07-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zar_lit', '0004_alter_zar_lit_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Имя')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
