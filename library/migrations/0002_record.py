# Generated by Django 3.2.9 on 2021-11-26 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqt', models.DateField()),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.kitob')),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.muallif')),
            ],
        ),
    ]
