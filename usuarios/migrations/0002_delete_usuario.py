# Generated by Django 4.0.1 on 2022-11-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_comentarios_usuario_alter_notasaulas_usuario'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]