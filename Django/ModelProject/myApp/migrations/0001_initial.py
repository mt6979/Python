# Generated by Django 2.0.2 on 2018-05-30 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateTimeField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.CharField(max_length=20)),
                ('scontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('createTime', models.DateField(auto_now_add=True)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Grades')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'students',
            },
        ),
    ]
