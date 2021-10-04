from django.contrib.auth import get_user, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from django.test import client
from .models import *
from . import forms

# Create your views here.
def index(request, *args, **kwargs):
    skills = None
    ins = None
    sent = None
    try:
        contact_form = forms.ContactForm()
        details = Detail.objects.get(pk=1)
        project_ = Project.objects.all()
        accomplish = Acomplishment.objects.get(pk=1)
        skills = [x.strip(",") for x in details.skills.split()]
        ins = Project.objects.get(pk=1)
        if request.method == 'POST':
            print("Tracking after post")
            contact_form = forms.ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.send()
                sent = True
                return render(request, "resume/index.html", dict(
                    details=details, project=project_, accom=accomplish, skills=skills,
                    ins=ins, sent=sent)
                    )
    except (Detail.DoesNotExist, Acomplishment.DoesNotExist):
        raise Http404
    return render(request, "resume/index.html", dict(
        details=details, project=project_, accom=accomplish, skills=skills,
        ins=ins, sent=sent, contact_form=contact_form
    )
                  )

def project(request, detail_pk, *args, **kwargs):
    try:
        project_ = Project.objects.get(pk=detail_pk)
    except Project.DoesNotExist:
        raise Http404
    return render(request, 'resume/project.html',
                  dict(
                      project=project_
                  )
                )

def sign_account(request, *args, **kwargs):
    form = forms.SignInForm()
    login_error = None

    if request.method == 'POST':
        form = forms.SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # Don't print out the password as a decent dev
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                if user.is_active:
                    login(request, user)
                    request.session["name"] = request.user.username
                    return redirect("resume:dashboard")
            else:
                login_error = "Opps! Only Isaiah Olaoye can access this platform."

    return render(request,
                  "resume/sign_in.html",
                  dict(
                      form=form,
                      login_error=login_error,
                  )
                  )

@login_required
def dashboard(request, *args, **kwargs):
    info = Detail.objects.get(personal_detail=get_user(request))
    info2 = Acomplishment.objects.get(pk=1)

    # template form  and modelform collection
    form = forms.ProjectForm()
    form_update = forms.DetailUpdateForm(instance=info)
    form_upd_accom = forms.AccomUpdateForm(instance=info2)

    if request.method == "POST":
        # Explicitly placing request.FILES helps to pick up the 
        # uploaded file in the form. without this, uploaded
        # files(image, file etc) won't be read
        form = forms.ProjectForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            name, topic = form.cleaned_data.get("name"), form.cleaned_data.get("topic")
            desc, created = form.cleaned_data.get("description"), form.cleaned_data.get("created")
            proj_url, client = form.cleaned_data.get("proj_url"), form.cleaned_data.get("client")

            if 'proj_pic' in request.FILES:
                proj_pic = request.FILES.get('proj_pic')

            ins = Project(name=name,
                          topic=topic,
                          description=desc,
                          proj_pic=proj_pic,
                          proj_url=proj_url,
                          client=client,
                          project_created=created
                          )

            ins.save()

            return redirect("resume:index")

    if request.method == "POST":
        form_update = forms.DetailUpdateForm(
            instance=info,
            data=request.POST,
            files=request.FILES
        )
        form_upd_accom = forms.AccomUpdateForm(
            instance=info2,
            data=request.POST
        )
        if form_update.is_valid() and form_upd_accom.is_valid():
            form_update.save()
            form_upd_accom.save()
            return redirect("resume:index")

    return render(
        request,
        "resume/dashboard.html",
        dict(
            form=form,
            form_update=form_update,
            form_upd_accom=form_upd_accom
        )
    )

@login_required
def sign_out_account(request, *args, **kwargs):
    logout(request)
    return redirect("resume:index")

def page_404(request, exception):
    return render(request, "404.svg")
