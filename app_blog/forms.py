from django import forms
from django.core.mail import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        context = f'Nome: {nome}\nEmail: {email}\nTelefone;' \
                  f' {telefone}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django',
            body=context,
            from_email='contato@funsion.com.br',
            to=['contato@funsion.com.br', ],
            headers={'Replay-to': email}
        )
        mail.send()
