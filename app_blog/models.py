from django.db import models

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField  # editor de texto para admin


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome da Categoria', max_length=100, null=False,
                            blank=False)
    estado = models.BooleanField('Ativa / Não Ativa', default=True)
    data_criacao = models.DateField('Criado', auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome.lower()


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do Autor', max_length=255, null=False,
                            blank=False)
    nick_name = models.CharField('Apelido do Autor ', max_length=255,
                                 null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    email = models.EmailField('Email', blank=False, null=False)
    estado = models.BooleanField('Autor está Ativo/Não está Ativo',
                                 default=True)
    data_criacao = models.DateField('Criado', auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.nome}'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=90, blank=False, null=False)
    slug = AutoSlugField(populate_from='titulo')
    descricao = models.CharField('Descrição', max_length=100,
                                 blank=False, null=False)
    conteudo = RichTextField()
    imagem = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Ativado / Desativado', default=True)
    data_criacao = models.DateField('Data Criação', auto_now=False,
                                    auto_now_add=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
