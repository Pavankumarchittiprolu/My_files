# Generated by Django 5.1.2 on 2024-11-28 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Dept',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
                ('sal', models.FloatField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dept')),
            ],
            options={
                'db_table': 'Emp',
            },
        ),
    ]
