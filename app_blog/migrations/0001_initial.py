# Generated by Django 2.2.8 on 2021-02-16 17:35

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Autor')),
                ('nick_name', models.CharField(max_length=255, verbose_name='Apelido do Autor ')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor está Ativo/Não está Ativo')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Criado')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Ativa / Não Ativa')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Criado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Título')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titulo')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Ativado / Desativado')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['titulo'],
            },
        ),
    ]
