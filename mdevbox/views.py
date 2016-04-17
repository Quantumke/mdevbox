from django.shortcuts import render, render_to_response,get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from mdevbox.forms import *
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader, Context
from django.contrib import messages
from .authentication import get_user_details
from .authentication import save_user

# Create your views here.
def new_profile(request):

    context = RequestContext(request)
    registered = False
    work_form = developersemployment(data=request.POST)
    edu_form=developerseducation(data=request.POST)
    portfolio_form=developersportfolio(data=request.POST)
    if request.method =='POST':
            data = {}
            get_user_details.GetUserDetails.run(request.POST, data)
            save_user.SaveUser.run(data)

            messages.success(request, "User Was registered successfully! An email confirmation email was sent!")
            return HttpResponseRedirect('/login')




    return render(request,
            'tabs.html',
            {'work_form':work_form, 'edu_form':edu_form, 'portfolio_form':portfolio_form,    'registered': registered},
            context_instance=RequestContext(request))

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('register.html',
                             context_instance=context)
