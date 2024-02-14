# Generated by Django 5.0.2 on 2024-02-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text_image',
            new_name='question_image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text_question',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Texto de la Pregunta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Respuesta C'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Respuesta D'),
        ),
    ]