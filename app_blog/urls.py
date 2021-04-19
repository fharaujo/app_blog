from django.urls import path

from .views import (IndexView,
                    GeralView,
                    PythonView,
                    ProgramacaoView,
                    DjangoView,
                    DetailViewPost,
                    ContatoView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('geral/', GeralView.as_view(), name='geral'),
    path('python/', PythonView.as_view(), name='python'),
    path('codar/', ProgramacaoView.as_view(), name='codar'),
    path('django/', DjangoView.as_view(), name='django'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('<str:slug>', DetailViewPost.as_view(), name='post'),


]