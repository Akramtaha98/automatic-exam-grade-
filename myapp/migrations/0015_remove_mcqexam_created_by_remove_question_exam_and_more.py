# Generated by Django 5.1.6 on 2025-03-03 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_mcqexam_examresult_question_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcqexam',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Default question text', max_length=200),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.question')),
            ],
        ),
        migrations.DeleteModel(
            name='ExamResult',
        ),
        migrations.DeleteModel(
            name='MCQExam',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
