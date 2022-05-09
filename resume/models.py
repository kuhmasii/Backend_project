from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class Detail(models.Model):
    personal_detail = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    _profile_pic = models.ImageField(
        upload_to='my_pics/', default="my_pics/avatar.png", null=True, blank=True)
    _backgroud_pic = models.ImageField(
        upload_to='my_pics/', default="my_pics/avatar.png", null=True, blank=True)
    about_me = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.personal_detail.username

    @property
    def profile_pic(self):
        try:
            url = self._profile_pic.url
        except ValueError:
            url = ''
        return url

    @property
    def backgroud_pic(self):
        try:
            url = self._backgroud_pic.url
        except ValueError:
            url = ''
        return url

    def get_projects(self):
        projects = self.project_owner.all()
        return projects


class Acomplishment(models.Model):
    work_completed = models.PositiveIntegerField(
        default=0, help_text='Total Work Completed')
    years_of_exper = models.PositiveIntegerField(
        default=0, help_text='Years of Experience.')
    total_client = models.PositiveIntegerField(
        default=0, help_text='Total Client Worked For.')
    award_won = models.PositiveIntegerField(default=0, help_text="Award Won.")

    def __str__(self):
        return str(self.pk)

    @property
    def accomplishment_update(self):

        experience = 2
        year = date.today().year
        if year == (year + 1):
            experience = self.years_of_exper + 1

        projects = Project.objects.all()
        project_count = projects.count()
        total_client = projects.exclude(
            client__iexact="Personal Project").count()

        self.work_completed = project_count
        self.total_client = total_client
        self.years_of_exper = experience
        self.save()


class Project(models.Model):
    owner = models.ForeignKey(
        Detail, on_delete=models.SET_NULL, null=True, related_name="project_owner")
    name = models.CharField(max_length=150, blank=False)
    topic = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True, null=True)
    _proj_pic = models.ImageField(
        upload_to='my_project_pics/', default="my_project_pics/cover.jpg", null=True, blank=True)
    proj_url = models.URLField()
    client = models.CharField(max_length=100, blank=True, null=True)
    project_created = models.DateTimeField()

    def __str__(self):
        return self.name

    @property
    def proj_pic(self):
        try:
            url = self._proj_pic.url
        except ValueError:
            url = ''
        return url

    class Meta:
        ordering = ("project_created",)
