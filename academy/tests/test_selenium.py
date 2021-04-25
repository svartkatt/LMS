from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

from academy.models import Student


class SeleniumTest(StaticLiveServerTestCase):

    NUMBER = 10

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    def setUp(self) -> None:
        self.user = User.objects.create(first_name='John', last_name='Doe')
        self._create_students(self.NUMBER)

    def _create_students(self, num):
        for i in range(num):
            Student.objects.create(
                first_name="John",
                last_name=f"Doe{str(i)}",
                email="somemail@gmail.com"
            )

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_unsuccessful_login(self):
        self.selenium.get(self.live_server_url + '/accounts/login/')

        login_url = self.selenium.find_element_by_id('login')
        login_url.click()

        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('test')

        submit_btn = self.selenium.find_element_by_id('input_login')
        submit_btn.submit()

        error = self.selenium.find_element_by_id('error')
        expected_error = "Your username and password didn't match. Please try again."
        self.assertEqual(error.text, expected_error)

    def test_sign_up(self):
        self.selenium.get(self.live_server_url + '/accounts/login/')

        sign_up_btn = self.selenium.find_element_by_id('sign_up')
        sign_up_btn.click()

        email_input = self.selenium.find_element_by_name('email')
        email_input.send_keys('test@mail.com')

        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_name('password1')
        password_input.send_keys('as79fssds2dhbd43gzsnfm9dsgbv7s')

        password_input = self.selenium.find_element_by_name('password2')
        password_input.send_keys('as79fssds2dhbd43gzsnfm9dsgbv7s')

        submit_btn = self.selenium.find_element_by_tag_name('button')
        submit_btn.submit()

        notification = self.selenium.find_element_by_id('notification')
        expected_notification = 'Please confirm your email address to complete the registration.'
        self.assertEqual(notification.text, expected_notification)

    def test_check_students_pagination(self):
        self.selenium.get(self.live_server_url)
        pagination = self.selenium.find_element_by_class_name('pagination')
        self.assertTrue(bool(pagination))

    def test_check_lecturers_pagination(self):
        self.selenium.get(self.live_server_url + '/lecturers')
        pagination = self.selenium.find_element_by_class_name('pagination')
        self.assertTrue(bool(pagination))

    def test_check_groups_pagination(self):
        self.selenium.get(self.live_server_url + '/groups')
        pagination = self.selenium.find_element_by_class_name('pagination')
        self.assertTrue(bool(pagination))

    def test_students_pagination_do_not_hide_for_single_page(self):
        Student.objects.all().delete()
        self._create_students(3)
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_class_name('page-link')

