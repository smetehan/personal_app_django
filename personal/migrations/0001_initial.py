# Generated by Django 4.1.5 on 2023-01-14 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(choices=[('Team Lead', 'LEAD'), ('Mid Lead', 'MID'), ('Junior', 'JUN')], max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'F'), ('Male', 'M'), ('Other', 'O'), ('Prefer Not Say', 'N')], max_length=50)),
                ('salary', models.IntegerField(default=1250)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personals', to='personal.department')),
            ],
        ),
    ]
