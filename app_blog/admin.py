from django.contrib import admin
from django.db import models

from .models import Categoria, Autor, Post

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    
    class Meta:
        model = Categoria


@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'estado', 'data_criacao')
    resource_class = CategoriaResource


class AutorResource(resources.ModelResource):
    
    class Meta:
        model = Autor


@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nome', 'nick_name', 'email']
    list_display = ('nome', 'nick_name', 'email', 'estado', 'data_criacao')
    resource_class = AutorResource


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'categoria', 'autor']
    list_display = ('titulo', 'autor', 'categoria', 'estado',
                    'data_criacao', 'slug')
    resources_class = PostResource
