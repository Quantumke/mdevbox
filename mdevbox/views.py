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
from .developer import get_work_details
from .developer import get_edu_details
from .developer import get_portfolio
from .developer import save_emp_details
from .developer import save_edu_details
from .developer import  save_portfolio
from .hire import get_form_data
from .hire import send_email_notification
from .hire import save_hire
from .jobs import get_form_data
from .jobs import save_job
from .jobs import apply_job
# Create your views here.



def new_profile(request):
    context = RequestContext(request)
    work_form = developersemployment(data=request.POST)
    portfolio_form=developersportfolio(data=request.POST)
    edu_form=developerseducation(data=request.POST)
    if request.method == 'POST':
            data = {}
            get_work_details.GetWorkDetails.run(request.POST, data)
            get_edu_details.GetEduDetails.run(request.POST, data)
            get_portfolio.GetPortfolio.run(request.POST, data)
            save_portfolio.SavePortfolio.run(data, request)
            save_emp_details.SaveEmpDetails.run(data, request)
            save_edu_details.SaveEduDetails.run(data, request)
            messages.success(request, "User Was registered successfully! An email confirmation email was sent!")
            return HttpResponseRedirect('/')




    return render(request,
            'tabs.html',
            {'work_form':work_form, 'portfolio_form':portfolio_form,'edu_form':edu_form },
            context_instance=RequestContext(request))



def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('register.html',
                             context_instance=context)

def fetch_one(request, id=1):
    return render_to_response('select.html',{'devs':developers_portfolio.objects.get(id=id) })


def fetch_all(request):
    return render_to_response('devs.html', {'devs': developers_portfolio.objects.all()})

def offer(request, id):
    if id:
        instance = developers_portfolio.objects.get(id=id)
        form = hire(request.POST or None, instance=instance)
        if form.is_valid():
            data ={}
            get_form_data.GetFormData.run(request.POST, data)
            send_email_notification.SendEmailNotification.run(data, id)
            save_hire.SaveHire.run(request, data)

            return HttpResponseRedirect('/')
        context = {
            "company": instance.portfoli_name,
            "instance": instance,
            "form":form,
        }
        return render(request, "make_offer.html", context)
def newjob(request):
    context = RequestContext(request)
    jobform = postjob(data=request.POST)
    if request.method == 'POST':
            data = {}
            get_form_data.GetFormData.run(request.POST, data)
            save_job.SaveJob.run(request,data)
            messages.success(request, "User Was registered successfully! An email confirmation email was sent!")
            return HttpResponseRedirect('/')




    return render(request,
            'postjob.html',
            {'jobform':jobform,  },
            context_instance=RequestContext(request))



def get_job(request, id=1):
    return render_to_response('viewjob.html',{'jobs':post_job.objects.get(id=id) })


def displayjobs(request):
    return render_to_response('all.html', {'jobs': post_job.objects.all()})

def applyjob(request, id):
    context = RequestContext(request)

    if id:

        data ={}
        apply_job.ApplyJob.run(data, request)
        messages.success(request, "Account was activated!")
        return render(request, "official/index.html", context)
