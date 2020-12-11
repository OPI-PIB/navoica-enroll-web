import pytest
import requests_mock
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.urls import reverse
from django_webtest import WebTest

from navoica_enroll.users.forms import UserRegistrationCourseEnglishForm, UserRegistrationCourseForm
from navoica_enroll.users.models import User
from navoica_enroll.users.views import UserRedirectView, UserUpdateView

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(self, user: User, request_factory: RequestFactory):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user: User, request_factory: RequestFactory):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:
    def test_get_redirect_url(self, user: User,
                              request_factory: RequestFactory):
        view = UserRedirectView()
        request = request_factory.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserEnrollView(WebTest):
    fixtures = ['users.json', 'socialaccount.json']
    course_id = 'course-v1:Test_Test+Test+2020_Test'

    def test_change_form_based_on_language(self):
        response = self.app.get(reverse('form', args=[self.course_id]))
        self.assertEqual(response.status_code, 302)

        User = get_user_model()
        user = User.objects.get(
            pk=1
        )
        self.assertEqual(user.username, 'admin')
        self.app.set_user(user)

        with requests_mock.Mocker() as mock:
            mock.get("{}{}{}".format(settings.NAVOICA_URL, "/api/courses/v1/courses/", self.course_id),
                     json={'course_id': self.course_id}, status_code=200)

            mock.get("{}{}{}".format(settings.NAVOICA_URL, "/api/enrollment/v1/enrollment/", self.course_id),
                     json={'is_active': False},
                     status_code=200)

            ###polish form
            response = self.app.get(reverse('form', args=[self.course_id]), headers={'Accept-Language': 'pl'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(type(response.context['form']), UserRegistrationCourseForm)
            # check if we have correct pdf files
            self.assertIn(settings.STATEMENT1_PDF, response.context['form'].fields['statement1'].label, )
            self.assertIn(settings.STATEMENT2_PDF, response.context['form'].fields['statement2'].label, )

            ###english form
            response = self.app.get(reverse('form', args=[self.course_id]), headers={'Accept-Language': 'en'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(type(response.context['form']), UserRegistrationCourseEnglishForm)
            # check if we have correct pdf files
            self.assertIn(settings.STATEMENT1_EN_PDF, response.context['form'].fields['statement1'].label, )
            self.assertIn(settings.STATEMENT2_EN_PDF, response.context['form'].fields['statement2'].label, )

    def test_register(self):
        User = get_user_model()
        user = User.objects.get(
            pk=1
        )
        self.assertEqual(user.username, 'admin')
        self.app.set_user(user)

        with requests_mock.Mocker() as mock:
            mock.get("{}{}{}".format(settings.NAVOICA_URL, "/api/courses/v1/courses/", self.course_id),
                     json={'course_id': self.course_id}, status_code=200)

            mock.get("{}{}{}".format(settings.NAVOICA_URL, "/api/enrollment/v1/enrollment/", self.course_id),
                     json={'is_active': False},
                     status_code=200)

            mock.post("{}{}".format(settings.NAVOICA_URL, "/api/enrollment/v1/enrollment"), status_code=200)

            response = self.app.get(reverse('form', args=[self.course_id]))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(type(response.context['form']), UserRegistrationCourseEnglishForm)

            d = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'gender': 'M',
                'pesel': '53022858449',
                'age': 30,
                'education': 3,
                'street': "Test",
                'street_no': "Test",
                'street_building_no': "Test",
                'postal_code': "00-001",
                'city': 'Szczecin',
                'voivodeship': 'west_pomerania',
                'county': 'szczecin',
                'country': 'Polska',
                'commune': 'Test',
                'phone': 432423,
                'email': 'longemaillongemaillongemaillongemail@longemaillongemaillongemaillongemail.pl',
                'status': 'Employed',
                'profession': 'Farmer',
                'work_name': "Test",
                'origin': "y",
                'homeless': "n",
                'disabled_person': "n",
                'social_disadvantage': "n",
                'statement1': True,
                'statement2': True

            }

            form = response.form
            for key, value in d.items():
                form[key] = value

            response = form.submit()
            self.assertEqual(response.status_code, 302)
            self.assertEqual(
                "{}/courses/{}?{}".format(settings.NAVOICA_URL, self.course_id, settings.NAVOICA_CAMPAIGN_URL),
                response.url)
