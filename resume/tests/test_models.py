from django.test import TestCase
from resume.models import Detail, Project
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
            project_created='2022-05-08'
        )

        check = ins.get_projects()

        self.assertTrue(check)
        self.assertIsInstance(check.first(), Project)
