from django.test import TestCase
from django.utils import timezone
from resume.models import Detail, Project, Acomplishment
from django.contrib.auth import get_user_model

User = get_user_model()


class DetailTests(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test',
            first_name='John',
            last_name='Doe',
            email='johndoe@yahoo.com',
            password='1234567890'
        )
        Detail.objects.create(
            personal_detail=user,
            about_me='I am a backend developer.'
        )

    def test_detail_creation(self):
        """Testing an instance of a Detail Model created.
                Instance should return the data of a User.username
                attribute as the '__str__' of the model, Detail.
        """
        ins = Detail.objects.get(pk=1)
        expected_value = ins.personal_detail.username

        self.assertIsInstance(ins, Detail)
        self.assertEqual(ins.__str__(), expected_value)

    def test_not_detail_creation(self):
        """Testing an instance of a Detail Model is not 
            yet created and the type is not of Detail Model.
        """
        ins = Detail.objects.get(pk=1)
        not_ins = 'This is a dummy data'

        self.assertNotIsInstance(not_ins, Detail)
        self.assertNotEqual(ins.__str__(), not_ins)

    def test_data_for_instance_of_detail_model(self):
        """Testing an instance data is correct
        """
        ins = Detail.objects.get(pk=1)

        self.assertEqual(ins.about_me, 'I am a backend developer.')

    def test_data_not_for_instance_of_detail_model(self):
        """Testing an instance data is not correct
        """
        ins = Detail.objects.get(pk=1)

        self.assertNotEqual(ins.about_me, 'I am a frontend developer')

    def test_profile_pic_property(self):
        """profile_pic property should return a url if a media path is given 
        or a media was selected.
        """
        ins = Detail.objects.get(pk=1)
        ins._profile_pic = 'my_pics/dummypicdata.png'
        ins.save()

        # calling the property function
        url = ins.profile_pic

        self.assertEqual(url, ins._profile_pic.url)

    def test_profile_pic_property_default(self):
        """profile_pic property should return the default media path if none is given 
           or a media was not selected.
        """
        ins = Detail.objects.get(pk=1)

        # calling the property function
        url = ins.profile_pic

        self.assertEqual(url, '/media/my_pics/avatar.png')

    def test_backgroud_pic_property(self):
        """backgroud_pic property should return a url if a media path is given 
           or a media was selected.
        """
        ins = Detail.objects.get(pk=1)
        ins._backgroud_pic = 'my_pics/dummybackground.png'
        ins.save()

        # calling the backgroud property function
        url = ins.backgroud_pic

        self.assertEqual(url, '/media/my_pics/dummybackground.png')

    def test_backgroud_pic_property_default(self):
        """backgroud_pic property should return the default media path if none is given 
           or a media was not selected.
        """
        ins = Detail.objects.get(pk=1)

        # calling the property function
        url = ins.backgroud_pic

        self.assertEqual(url, '/media/my_pics/avatar.png')

    def test_get_projects_with_value(self):
        """
        get_projects method should return a query.
        """
        ins = Detail.objects.get(pk=1)
        check = ins.get_projects()

        self.assertFalse(check)

    def test_get_projects_without_value(self):
        """
        get_projects method should return an empty query.
        """
        ins = Detail.objects.get(pk=1)
        project = Project.objects.create(
            owner=ins, name='FistProject',
            topic='Testing Project',
            project_created=timezone.now()
        )

        check = ins.get_projects()

        self.assertTrue(check)
        self.assertIsInstance(check.first(), Project)


class AcomplishmentTests(TestCase):
    def setUp(self):
        Acomplishment.objects.create(
            years_of_exper=2
        )

    def test_accom_creation(self):
        """Testing an instance of an Acomplishment Model created.
            Instance should return the data of the pk field
            attribute as the '__str__' of the model, Acomplishment.
        """
        ins = Acomplishment.objects.get(pk=1)

        self.assertIsInstance(ins, Acomplishment)
        self.assertEqual(ins.__str__(), str(ins.pk))

    def test_accom_not_creation(self):
        """Testing an instance of a Acomplishment Model that is not 
            yet created and the type is not of Acomplishment Model.
        """
        ins = Acomplishment.objects.get(pk=1)
        not_ins = 'This is a dummy data'

        self.assertNotIsInstance(not_ins, Acomplishment)
        self.assertNotEqual(ins.__str__(), not_ins)

    def test_accomplishment_update_before(self):
        """Testing accomplishment_update default values
           of the fields should be return before calling 
           the function
        """

        ins = Acomplishment.objects.get(pk=1)

        self.assertEqual(ins.work_completed, 0)
        self.assertEqual(ins.years_of_exper, 2)
        self.assertEqual(ins.total_client, 0)

    def test_accomplishment_update(self):
        """Testing accomplishment_update default values
           should be updated after calling 
           the function
        """
        project = Project.objects.create(
            name='FistProject',
            topic='Testing Project',
            client='Testing',
            project_created=timezone.now()
        )
        ins = Acomplishment.objects.get(pk=1)
        ins.accomplishment_update

        self.assertEqual(ins.work_completed, 1)
        self.assertEqual(ins.years_of_exper, 2)
        self.assertEqual(ins.total_client, 1)

    def test_accomplishment_update_if_personal_project(self):
        """Testing accomplishment_update should not update
           the total_client if the client is 'Personal Project' 
        """
        project = Project.objects.create(
            name='FistProject',
            topic='Testing Project',
            client='Personal Project',
            project_created=timezone.now()
        )
        ins = Acomplishment.objects.get(pk=1)
        ins.accomplishment_update

        self.assertEqual(ins.work_completed, 1)
        self.assertEqual(ins.years_of_exper, 2)
        self.assertEqual(ins.total_client, 0)


class ProjectTests(TestCase):
    def setUp(self):
        Project.objects.create(
            name='Testing Project',
            topic='Atomation',
            project_created=timezone.now()
        )
    def test_project_creation(self):
        """Testing an instance of an Project Model created.
            Instance should return the data of the name field
            attribute as the '__str__' of the model, Project.
        """
        ins = Project.objects.get(pk=1)

        self.assertIsInstance(ins, Project)
        self.assertEqual(ins.__str__(), 'Testing Project')

    def test_accom_not_creation(self):
        """Testing an instance of a Project Model that is not 
            yet created and the type is not of Project Model.
        """
        ins = Project.objects.get(pk=1)
        not_ins = 'This is a dummy data'

        self.assertNotIsInstance(not_ins, Project)
        self.assertNotEqual(ins.__str__(), not_ins)
        
    def test_proj_pic_property(self):
        """proj_pic property should return a url if a media path is given 
        or a media was selected.
        """
        ins = Project.objects.get(pk=1)
        ins._proj_pic = 'my_project_pics/dummyprof_pic.png'
        ins.save()

        # calling the property function
        url = ins.proj_pic

        self.assertEqual(url, '/media/my_project_pics/dummyprof_pic.png')

    def test_proj_pic_property_default(self):
        """proj_pic property should return the default media path if none is given 
           or a media was not selected.
        """
        ins = Project.objects.get(pk=1)

        # calling the property function
        url = ins.proj_pic

        self.assertEqual(url, '/media/my_project_pics/cover.jpg')