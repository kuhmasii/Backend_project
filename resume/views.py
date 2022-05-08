from django.contrib.auth import get_user, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from . import forms


def index(request, *args, **kwargs):

    sent, skills = None, None
    contact_form = forms.ContactForm()
    try:
        accom = Acomplishment.objects.get(pk=1)
        details = Detail.objects.get(pk=1)
        print(details.get_projects())
        accom.accomplishment_update
        skills = [x.strip(",") for x in details.skills.split()]
    except (Detail.DoesNotExist, Acomplishment.DoesNotExist):
        raise Http404

    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.send()
            sent = True
            context = {'accom': accom, 'details': details,
                       'sent': sent, 'skills': skills}
            return render(request, "resume/index.html", context)

    context = {'accom': accom, 'details': details, 'sent': sent,
               'skills': skills, 'contact_form': contact_form}
    return render(request, "resume/index.html", context)


def project(request, detail_pk, *args, **kwargs):
    try:
        project = Project.objects.get(pk=detail_pk)
    except Project.DoesNotExist:
        raise Http404
    context = {'project': project}
    return render(request, 'resume/project.html', context)


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
                login(request, user)
                return redirect("resume:resume-dashboard")
            else:
                login_error = "Opps! Only Isaiah Olaoye can access this platform."

    context = {"form": form, 'login_error': login_error}
    return render(request, "resume/sign_in.html", context)


@login_required
def dashboard(request, *args, **kwargs):
    owner = Detail.objects.get(personal_detail=get_user(request))
    owner_accom = Acomplishment.objects.get(pk=1)

    # template form  and modelform collection
    form = forms.ProjectForm()
    form_update = forms.DetailUpdateForm(instance=owner)
    form_upd_accom = forms.AccomUpdateForm(instance=owner_accom)

    if request.method == "POST":
        # Explicitly placing request.FILES helps to pick up the
        # uploaded file in the form. without this, uploaded
        # files(image, file etc) won't be read
        form = forms.ProjectForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            topic = form.cleaned_data.get("topic")
            desc = form.cleaned_data.get("description")
            created = form.cleaned_data.get("created")
            proj_url = form.cleaned_data.get("proj_url")
            client = form.cleaned_data.get("client")

            if 'proj_pic' in request.FILES:
                proj_pic = request.FILES.get('proj_pic')

            Project.objects.create(
                owner=owner,
                name=name,
                topic=topic,
                description=desc,
                _proj_pic=proj_pic,
                proj_url=proj_url,
                client=client,
                project_created=created
            )
            return redirect("resume:resume-list")

    if request.method == "POST":
        form_update = forms.DetailUpdateForm(
            instance=owner,
            data=request.POST,
            files=request.FILES
        )
        form_upd_accom = forms.AccomUpdateForm(
            instance=owner_accom,
            data=request.POST
        )

        if form_update.is_valid() and form_upd_accom.is_valid():
            form_update.save()
            form_upd_accom.save()
            return redirect("resume:resume-list")

    context = {"form": form, "form_update": form_update,
               "form_upd_accom": form_upd_accom}
    return render(request, "resume/dashboard.html", context)


@login_required
def sign_out_account(request, *args, **kwargs):
    logout(request)
    return redirect("resume:resume-list")


def page_404(request, exception):
    return render(request, "404.svg")
