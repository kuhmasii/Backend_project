from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from resume.models import Project, Detail, Acomplishment

User = get_user_model()


class ResumeIndexTests(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test',
            first_name='John',
            last_name='Doe',
            email='johndoe@yahoo.com',
            password='1234567890'
        )
        user.set_password(user.password)
        user.save()

        detail = Detail.objects.create(
            personal_detail=user,
            about_me='I am a backend developer.',
            skills='Django, DRF'
        )
        project = Project.objects.create(
            owner=detail,
            name='Testing Project',
            topic='Atomation',
            project_created=timezone.now()

        )
        Acomplishment.objects.create(
            years_of_exper=2
        )

    def test_index_view(self):
        """Most component of the website
        is displayed, the projects, contact,
        accomplishment and information.
        """

        accom = Acomplishment.objects.get(pk=1)
        details = Detail.objects.get(pk=1)

        response = self.client.get(reverse('resume:resume-list'))

        form = response.context['contact_form'].data

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['sent'])
        self.assertFalse(form.dict())
        self.assertEqual(response.context['skills'], ['Django', 'DRF'])
        self.assertContains(response, 'I am a backend developer.')
        self.assertQuerysetEqual([response.context["details"]], [details])
        self.assertQuerysetEqual([response.context["accom"]], [accom])
        self.assertTemplateUsed(response, "resume/index.html")

    def test_index_post_view(self):
        """component of the website should
        be displayed when an email is sent.
        """

        accom = Acomplishment.objects.get(pk=1)
        details = Detail.objects.get(pk=1)

        data = {'email': 'test@gmail.com', 'name': 'Test',
                'message': 'This is a test', 'subject': 'TESTING'}
        response = self.client.post(reverse('resume:resume-list'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['sent'])
        self.assertEqual(response.context['skills'], ['Django', 'DRF'])
        self.assertContains(response, 'I am a backend developer.')
        self.assertQuerysetEqual([response.context["details"]], [details])
        self.assertQuerysetEqual([response.context["accom"]], [accom])
        self.assertTemplateUsed(response, "resume/index.html")

    def test_project_view(self):
        """project should return a detail
                provided by the id.
        """
        obj = Project.objects.get(pk=1)

        response = self.client.get(reverse(
            'resume:resume-detail', args=(obj.id,)),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing Project")
        self.assertTemplateUsed(response, "resume/project.html")
        self.assertQuerysetEqual([response.context["project"]], [obj])

    def test_project_view_not_found(self):
        """
        project provided if the id not correct.        
        Project view should not return a detail
        """
        try:
            response = self.client.get(
                reverse(
                    "resume:resume-detail",
                    args=(999,),
                )
            )
        except:
            self.assertEqual(response.status_code, 404)

    def test_sign_account_view_get_method(self):
        """View should send a user to the
        login page if not yet authenticated.
        """

        response = self.client.get(
            reverse("resume:resume-login")
        )

        form = response.context['form'].data

        self.assertEqual(response.status_code, 200)
        self.assertFalse(form.dict())
        self.assertFalse(response.context['login_error'])
        self.assertTemplateUsed(response, 'resume/sign_in.html')

    def test_sign_account_view_post_method(self):
        """View should return a user to the 
           signup page when the user information is not correct.
        """
        user = User.objects.get(pk=1)
        data = {"username": user.username, "password": 'passwordnan'}
        response = self.client.post(reverse("resume:resume-login"), data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['login_error'], 'Opps! Only Isaiah Olaoye can access this platform.')
        self.assertTemplateUsed(response, 'resume/sign_in.html')

    def test_sign_account_view_post_method_correct_data(self):
        """View should return a user to the dashboard page
           when the user information is correct.
        """
        user = User.objects.get(pk=1)
        data = {"username": user.username, "password": "1234567890"}
        response = self.client.post(reverse("resume:resume-login"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('resume:resume-dashboard'))

    def test_sign_out_account(self):
        """Should sign out authenticated user"""

        user = User.objects.get(pk=1)
        data = {"username": user.username, "password": "1234567890"}
        self.client.login(**data)

        response = self.client.get(reverse('resume:resume-logout'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('resume:resume-list'))
