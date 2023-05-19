# Generated by Django 4.2 on 2023-05-19 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_admin_user_first_name_user_is_staff_user_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('schedule', models.DateField()),
                ('semester', models.IntegerField()),
                ('min_students', models.IntegerField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.career')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(through='system.Enrollment', to='system.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.teacher'),
        ),
    ]