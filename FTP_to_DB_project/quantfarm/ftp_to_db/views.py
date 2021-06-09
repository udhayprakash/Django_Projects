from django.views.generic import CreateView, UpdateView, DetailView
from ftp_to_db.models import FTPCredentials
from ftp_to_db.forms import FTPCredentialsForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

class FTPCredentialsCreateView(CreateView):
    model = FTPCredentials
    fields = ('ftp_url', 'ftp_username', 'ftp_password', 'ftp_filename')
    template_name = 'ftp_to_db/ftpcredentials_form.html'


class FTPCredentialsUpdateView(UpdateView):
    model = FTPCredentials
    form_class = FTPCredentialsForm
    template_name = 'ftp_to_db/ftpcredentials_update_form.html'
    

def detail(request, question_id):
    etl_job = get_object_or_404(FTPCredentials, pk=question_id)
    return render(request, 'ftp_to_db/detail.html', {'etl_job': etl_job})
