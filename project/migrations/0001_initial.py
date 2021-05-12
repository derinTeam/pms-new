# Generated by Django 3.1.7 on 2021-04-07 21:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('p_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100, verbose_name='Proje İsmi')),
                ('efforts', models.DurationField(verbose_name='Projenin Süresi')),
                ('projectStatus', models.CharField(choices=[('1', 'Durdu'), ('2', 'Çalışıyor'), ('3', 'Bitti')], default=1, max_length=7, verbose_name='Proje Durumu')),
                ('dead_line', models.DateField(verbose_name='Projenin Bitiş Tarihi')),
                ('projectPoint', models.IntegerField(default=1, verbose_name='Proje Puanı')),
                ('complete_per', models.FloatField(max_length=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Tamamlanma Performansı (100 üzerinden)')),
                ('description', models.TextField(blank=True, verbose_name='Proje Açıklaması')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_manager.company', verbose_name='Proje Sahibi Şirket')),
                ('employees', models.ManyToManyField(to='employee.Employee', verbose_name='Çalışacaklar')),
                ('projectManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_manager.projectmanager', verbose_name='Projenin Yöneticisi')),
            ],
            options={
                'ordering': ['projectName'],
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('status', models.CharField(choices=[('1', 'Durdu'), ('2', 'Çalışıyor'), ('3', 'Bitti')], default=1, max_length=7)),
                ('due', models.CharField(choices=[('1', 'Zamanı Yaklaşıyor'), ('2', 'Zamanı Aştı'), ('3', 'Bitti')], default=1, max_length=7)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('employees', models.ManyToManyField(to='employee.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projects')),
                ('tasksManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_manager.projectmanager')),
            ],
            options={
                'ordering': ['project', 'task_name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectEmployee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Proje Çalışanı')),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projects', verbose_name='Proje İsmi')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerEmployees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Çalışan')),
                ('managers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_manager.projectmanager', verbose_name='Yönetici')),
            ],
        ),
    ]
