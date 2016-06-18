from django.shortcuts import render_to_response
from django.template import RequestContext
from circon.configuration.authenticate.forms import LoginForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import auth


def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():  # next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/Admin')
                else:
                    mensaje = "usuario y/o password incorrecto"
        # next = reuest.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form': form, 'mensaje': mensaje}
        return render_to_response('configuration/authenticate/login.html',
                                  ctx,
                                  context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
