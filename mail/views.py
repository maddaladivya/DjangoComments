# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import smtplib
# Create your views here.
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from mail.models import Email_details, Reply


def send(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('Email')
        comment = request.POST.get('comment')
        u = Email_details.objects.create(name=name, email=email, comment = comment)
        u.save()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('sarvanimini@gmail.com','mini@241098')
        mail.sendmail('sarvanimini@gmail.com','maddaladivya3212@gmail.com',comment)
        mail.close()
        temp1 = 'mail/mail.html'
        return render(request,temp1,{})
    temp = 'mail/mail.html'
    return render(request,temp,{})

class Comment(ListView):
    temp = 'mail/email_details_list.html'
    model = Email_details
    def get_context_data(self, **kwargs):
        context = super(Comment, self).get_context_data(**kwargs)
        context['roles'] = Reply.objects.all()
        # And so on for more models
        return context

def reply(request,ak):
    a = Email_details.objects.get(id=ak)
    if request.method == "POST":
        comment = Email_details.objects.get(id=ak)
        reply = request.POST.get('reply')
        u = Reply.objects.create(comments=comment, reply=reply)
        print "Divya"
        u.save()
        return HttpResponseRedirect('/mail/display')
    return render(request,'mail/reply.html',{'a':a})
