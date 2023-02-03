from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


from mailing_service.models import Mssg, Client


def mailing(request):
    emails = ['andreymazo@mail.ru', 'andreymazo2@mail.ru']
    # for i in emails:
    if request.method == 'GET':
        res = "Zaglushka chtobi ne otpravlyat pisma"
        # res = send_mail(
        #     subject=' test subject ',
        #     message=f' test message ',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=emails,
        #     fail_silently=False,
        #     # auth_user=None,
        #     # auth_password=None,
        #     # connection=None,
        #     # html_message=None,
        # )

        # context = {'object_list': Mssg.objects.all()}
        print(f'Messg sent >>>>>>, Result, {res}')
        context = {'res':res}
        return render(request, 'mailing_service/index.html', context)

class MssgListView(ListView):
    model = Mssg

class ClientListView(ListView):
    model = Client

# class ClientRegisterView(CreateView):
#     model = Client
#     form_class = ClientCreationForm
#     template_name = "/user_form.html"
#     # success_url = "/"
#     success_url = reverse_lazy('mailing_service:client')
# def Mssg(request):
#     context = {'object_list': Mssg.objects.all()}
#     return render(request, 'mailing_service/index.html', context)




# from django.views.generic.base import TemplateView
#
#
# class HomePageView(TemplateView):
#
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # здесь передаем переменную с именем name_variable
#         # и ее значением value_variable
#         context['name_variable'] = "value_variable"
#         return context


