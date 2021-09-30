from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Detail(models.Model):
    personal_detail = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    phone_number = models.IntegerField(default=00000000000)
    address = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to='my_pics/', blank=False)
    about_me = models.TextField(blank=True)
    skills = models.CharField(max_length=150, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personal_detail.username} is Your Username, {self.personal_detail.first_name} {self.personal_detail.last_name}"

    @property
    def profileURL(self):
        try:
            url = self.profile_pic.url
        except ValueError:
            url = ''
        return url

class Acomplishment(models.Model):
    personal_detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="acomplishment")
    work_completed = models.IntegerField(default=0, help_text='Total Work Completed')
    years_of_exper = models.IntegerField(default=0, help_text='Years of Experience.')
    total_client = models.IntegerField(default=0, help_text='Total Client Worked For.')
    award_won = models.IntegerField(default=0, help_text="Award Won.")

    def __str__(self):
        return  str(self.pk)

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False)
    topic = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    proj_pic = models.ImageField(upload_to='my_project_pics/', blank=False, null=False)
    proj_url = models.URLField()
    client = models.CharField(max_length=100, blank=True)
    project_created = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_total_accom(self):
        return len(
            Project.objects.all()
        )
    
    def get_total_client(self):
        ins = Project.objects.all()
        total_client = [x for x in ins if x.client != "Personal Project"]
        return len(total_client)

    @property
    def ProjectURL(self):
        try:
            url = self.proj_pic.url
        except ValueError:
            url = ''
        return url

    class Meta:
        ordering = ("project_created",)