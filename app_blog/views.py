from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Post, Categoria
from .forms import ContatoForm
from django.contrib import messages


# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self):
        post = Post.objects.all()
        q = self.request.GET.get('buscar',)

        if q:
            post = Post.objects.filter(
                Q(titulo__icontains=q) |
                Q(descricao__icontains=q) |
                Q(autor__nome__icontains=q)
            ).order_by('-data_criacao').distinct()
        else:
            post = Post.objects.filter(estado=True)
        return post


class GeralView(ListView):
    model = Post
    template_name = 'geral.html'
    queryset = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nome__iexact='Geral')
    )
    context_object_name = 'geral'


class PythonView(ListView):
    model = Post
    template_name = 'python.html'
    queryset = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nome__iexact='Python')
    )
    context_object_name = 'python'


class ProgramacaoView(ListView):
    model = Post
    template_name = 'programacao.html'
    queryset = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nome__iexact='Codar')
    )
    context_object_name = 'codar'


class DjangoView(ListView):
    model = Post
    template_name = 'django.html'
    queryset = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nome__iexact='Django')
    )
    context_object_name = 'django'


class DetailViewPost(DetailView):
    try:
        model = Post
        template_name = 'post.html'
        context_object_name = 'post'
    except Post.DoesNotExist:
        raise Http404


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(ContatoView, self).form_valid(form)

        # formulário se for inválido

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail.')
        return super(ContatoView, self).form_invalid(form)
