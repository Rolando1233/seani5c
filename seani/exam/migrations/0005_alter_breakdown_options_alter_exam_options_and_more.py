# Generated by Django 5.0.2 on 2024-03-12 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_alter_breakdown_correct'),
        ('library', '0004_alter_module_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breakdown',
            options={},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'examen', 'verbose_name_plural': 'examenes'},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': 'etapa', 'verbose_name_plural': 'etapas'},
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question',
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='exam.BreakDown', to='library.question', verbose_name='Preguntas'),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='correct',
            field=models.CharField(default='-', max_length=5, verbose_name='Respuesta correcta'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module', verbose_name='Módulos'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Módulo'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='application_date',
            field=models.DateField(verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage',
            field=models.IntegerField(verbose_name='Etapa'),
        ),
    ]