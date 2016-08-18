from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, RedirectView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "configuration/authenticate/login.html"
    success_url = reverse_lazy("start_view")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'index_view'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


# def login_view(request):
#     mensaje = ""
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/')
#     else:
#         if request.method == "POST":
#             form = LoginForm(request.POST)
#             if form.is_valid():  # next = request.POST['next']
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = auth.authenticate(username=username, password=password)
#                 if user is not None and user.is_active:
#                     auth.login(request, user)
#                     return HttpResponseRedirect('/Admin')
#                 else:
#                     mensaje = "usuario y/o password incorrecto"
#         # next = reuest.REQUEST.get('next')
#         form = LoginForm()
#         ctx = {'form': form, 'mensaje': mensaje}
#         return render_to_response('configuration/authenticate/login.html',
#                                   ctx,
#                                   context_instance=RequestContext(request))
#
#
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')
