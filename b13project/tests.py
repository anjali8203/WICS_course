# # test for txt
# # from moto import mock_s3
# # import boto3
# # from django.core.files.uploadedfile import SimpleUploadedFile
# # from django.test import TestCase
# # from django.urls import reverse
# # from django.conf import settings
# # from .models import UploadedFile
# #
# # class FileUploadTest(TestCase):
# #
# #     @mock_s3
# #     def test_file_upload(self):
# #         # Set the bucket name
# #         bucket_name = 'test-bucket'
# #
# #         # Mock the S3 service and create a bucket in the mocked environment
# #         s3 = boto3.resource('s3', region_name='us-east-1')
# #         s3.create_bucket(Bucket=bucket_name)
# #
# #         # Override the AWS settings for the test environment
# #         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
# #         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
# #         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
# #         settings.AWS_S3_REGION_NAME = 'us-east-1'
# #         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing
# #
# #         # Prepare a simple file for upload
# #         file = SimpleUploadedFile("test.txt", b"file content", content_type="text/plain")
# #
# #         # Post the file to the file upload view
# #         response = self.client.post(reverse('file_upload'), {'file': file})
# #
# #         # Check if the upload was successful
# #         self.assertEqual(response.status_code, 302)
# #
# #         # Check if the file was uploaded to the mocked S3 bucket
# #         objects = s3.Bucket(bucket_name).objects.all()
# #         self.assertTrue(any(obj.key == 'uploads/test.txt' for obj in objects))

# # test for pdf
# # from moto import mock_s3
# # import boto3
# # from django.core.files.uploadedfile import SimpleUploadedFile
# # from django.test import TestCase
# # from django.urls import reverse
# # from django.conf import settings
# # from .models import UploadedFile
# #
# # class FileUploadTest(TestCase):
# #
# #     @mock_s3
# #     def test_file_upload(self):
# #         # Set the bucket name
# #         bucket_name = 'test-bucket'
# #
# #         # Mock the S3 service and create a bucket in the mocked environment
# #         s3 = boto3.resource('s3', region_name='us-east-1')
# #         s3.create_bucket(Bucket=bucket_name)
# #
# #         # Override the AWS settings for the test environment
# #         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
# #         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
# #         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
# #         settings.AWS_S3_REGION_NAME = 'us-east-1'
# #         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing
# #
# #         # Prepare a PDF file for upload
# #         file = SimpleUploadedFile("test.pdf", b"file content", content_type="application/pdf")
# #
# #         # Post the file to the file upload view
# #         response = self.client.post(reverse('file_upload'), {'file': file})
# #
# #         # Check if the upload was successful
# #         self.assertEqual(response.status_code, 302)
# #
# #         # Check if the file was uploaded to the mocked S3 bucket
# #         objects = s3.Bucket(bucket_name).objects.all()
# #         self.assertTrue(any(obj.key == 'uploads/test.pdf' for obj in objects))

# # test for jpg
# from moto import mock_s3
# import boto3
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from django.conf import settings
# from .models import UploadedFile

# class FileUploadTest(TestCase):

#     @mock_s3
#     def test_jpg_file_upload(self):
#         # Set the bucket name
#         bucket_name = 'test-bucket'

#         # Mock the S3 service and create a bucket in the mocked environment
#         s3 = boto3.resource('s3', region_name='us-east-1')
#         s3.create_bucket(Bucket=bucket_name)

#         # Override the AWS settings for the test environment
#         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
#         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
#         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
#         settings.AWS_S3_REGION_NAME = 'us-east-1'
#         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing

#         # Prepare a JPEG file for upload
#         file = SimpleUploadedFile("test.jpg", b"fake image content", content_type="image/jpeg")

#         # Post the file to the file upload view
#         response = self.client.post(reverse('file_upload'), {'file': file})

#         # Check if the upload was successful
#         self.assertEqual(response.status_code, 302)

#         # Check if the file was uploaded to the mocked S3 bucket
#         objects = s3.Bucket(bucket_name).objects.all()
#         self.assertTrue(any(obj.key == 'uploads/test.jpg' for obj in objects))




#### new below 




# test for txt
# from moto import mock_s3
# import boto3
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from django.conf import settings
# from .models import UploadedFile
#
# class FileUploadTest(TestCase):
#
#     @mock_s3
#     def test_file_upload(self):
#         # Set the bucket name
#         bucket_name = 'test-bucket'
#
#         # Mock the S3 service and create a bucket in the mocked environment
#         s3 = boto3.resource('s3', region_name='us-east-1')
#         s3.create_bucket(Bucket=bucket_name)
#
#         # Override the AWS settings for the test environment
#         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
#         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
#         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
#         settings.AWS_S3_REGION_NAME = 'us-east-1'
#         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing
#
#         # Prepare a simple file for upload
#         file = SimpleUploadedFile("test.txt", b"file content", content_type="text/plain")
#
#         # Post the file to the file upload view
#         response = self.client.post(reverse('file_upload'), {'file': file})
#
#         # Check if the upload was successful
#         self.assertEqual(response.status_code, 302)
#
#         # Check if the file was uploaded to the mocked S3 bucket
#         objects = s3.Bucket(bucket_name).objects.all()
#         self.assertTrue(any(obj.key == 'uploads/test.txt' for obj in objects))

# test for pdf
# from moto import mock_s3
# import boto3
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from django.conf import settings
# from .models import UploadedFile
#
# class FileUploadTest(TestCase):
#
#     @mock_s3
#     def test_file_upload(self):
#         # Set the bucket name
#         bucket_name = 'test-bucket'
#
#         # Mock the S3 service and create a bucket in the mocked environment
#         s3 = boto3.resource('s3', region_name='us-east-1')
#         s3.create_bucket(Bucket=bucket_name)
#
#         # Override the AWS settings for the test environment
#         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
#         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
#         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
#         settings.AWS_S3_REGION_NAME = 'us-east-1'
#         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing
#
#         # Prepare a PDF file for upload
#         file = SimpleUploadedFile("test.pdf", b"file content", content_type="application/pdf")
#
#         # Post the file to the file upload view
#         response = self.client.post(reverse('file_upload'), {'file': file})
#
#         # Check if the upload was successful
#         self.assertEqual(response.status_code, 302)
#
#         # Check if the file was uploaded to the mocked S3 bucket
#         objects = s3.Bucket(bucket_name).objects.all()
#         self.assertTrue(any(obj.key == 'uploads/test.pdf' for obj in objects))

# # test for jpg
# from moto import mock_aws
# import boto3
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from django.conf import settings
# from .models import UploadedFile

# class FileUploadTest(TestCase):

#     @mock_aws
#     def test_jpg_file_upload(self):
#         # Set the bucket name
#         bucket_name = 'test-bucket'

#         # Mock the S3 service and create a bucket in the mocked environment
#         s3 = boto3.resource('s3', region_name='us-east-1')
#         s3.create_bucket(Bucket=bucket_name)

#         # Override the AWS settings for the test environment
#         settings.AWS_STORAGE_BUCKET_NAME = bucket_name
#         settings.AWS_ACCESS_KEY_ID = 'test-access-key'
#         settings.AWS_SECRET_ACCESS_KEY = 'test-secret-key'
#         settings.AWS_S3_REGION_NAME = 'us-east-1'
#         settings.AWS_DEFAULT_ACL = None  # Disable ACL for testing

#         # Prepare a JPEG file for upload
#         file = SimpleUploadedFile("test.jpg", b"fake image content", content_type="image/jpeg")

#         # Post the file to the file upload view
#         response = self.client.post(reverse('file_upload'), {'file': file})

#         # Check if the upload was successful
#         self.assertEqual(response.status_code, 302)

#         # Check if the file was uploaded to the mocked S3 bucket
#         objects = s3.Bucket(bucket_name).objects.all()
#         self.assertTrue(any(obj.key == 'uploads/test.jpg' for obj in objects))
###############################################################################


from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from .models import Project, UploadedFile
from .models import UserProfile



class UserAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'password123'

    def test_user_registration_and_login(self):
        # Register the user
        User.objects.create_user(username=self.username, password=self.password)
        #Login is successful
        login_successful = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login_successful)

    def test_user_login_failure_without_credentials(self):
        #log in with incorrect credentials
        login_successful = self.client.login(username=self.username, password='wrongpassword')
        self.assertFalse(login_successful)

    def test_user_registration_failure_with_existing_username(self):
        # Attempt to register with the same username
        User.objects.create_user(username=self.username, password=self.password)  # Existing user
        with self.assertRaises(Exception):
            User.objects.create_user(username=self.username, password='newpassword')

    def test_password_change(self):
        # Change password
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        self.new_password = 'newpassword123'
        self.user.set_password(self.new_password)
        self.user.save()
        self.client.logout()

        # Log in with new password
        login_successful = self.client.login(username=self.username, password=self.new_password)
        self.assertTrue(login_successful)


#Testing for Anonymous Login 
class AnonymousLoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_anonymous_login_creates_session(self):
        # Send a request to the anonymous_login view
        response = self.client.get(reverse('anonymous_login'))
        # session key is created
        self.assertTrue(self.client.session.session_key)
        # session contains the anonymous_user flag
        self.assertTrue(self.client.session.get('anonymous_user', False))
        # Check that the response is a redirect to the homepage
        self.assertRedirects(response, reverse('anonymous_project_list'))

    #Testing if clicking different pages will impact Anonymous user's session key
    def test_anonymous_login_existing_session(self):
        self.client.get(reverse('homepage'))
        # Store the existing session key
        current_session_key = self.client.session.session_key
        response = self.client.get(reverse('anonymous_login'))
        # Check that the session key remains the same
        self.assertEqual(self.client.session.session_key, current_session_key)
        self.assertTrue(self.client.session.get('anonymous_user', False))
        self.assertRedirects(response, reverse('anonymous_project_list'))

#Password checking for all possible test cases
class PasswordValidation(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'password123'  #This will throw an error -> password does not meet credentials

    def test_password_too_short(self):
        password = 'short'
        with self.assertRaises(ValidationError):
            validate_password(password)

    def test_password_too_similar(self):
        #password can't be the same as the username
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        password = 'testuser123'
        with self.assertRaises(ValidationError):
            validate_password(password, user=user)

    def test_password_common(self):
        password = 'password123'
        with self.assertRaises(ValidationError):
            validate_password(password)

    def test_password_entirely_numeric(self):
        password = '12345678'
        with self.assertRaises(ValidationError):
            validate_password(password)

    def test_password_with_special_characters(self):
        #special characters -> expected to pass
        password = 'Password_is_Complex@skyt1acker'
        try:
            validate_password(password)
        except ValidationError:
            self.fail("validate_password() raised ValidationError unexpectedly!")

    def test_password_with_whitespace(self):
        # leading/trailing whitespace -> expected to fail
        password = '  password123  '
        with self.assertRaises(ValidationError):
            validate_password(password)

    def empty_password(self):
        #password is empty -> fail
        password = ' '
        with self.assertRaises(ValidationError):
            validate_password(password)        

    def test_password_with_unicode_characters(self):
        # Test a password with unicode characters
        password = 'Pässwörd123_unique'
        try:
            validate_password(password)
        except ValidationError:
            self.fail("validate_password() raised ValidationError unexpectedly!")

    def test_password_with_mixed_case(self):
        # Test a password with mixed case that should pass validation
        password = 'Password_WiLl_WoRkXD$'
        try:
            validate_password(password)
        except ValidationError:
            self.fail("validate_password() raised ValidationError unexpectedly!")


#Testing view_profile -> ensuring function is correct 
class ViewProfileViewTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.client = Client()
    #if a user -> redirect to user's "view profile" page
    def test_view_profile_with_existing_profile(self):
        UserProfile.objects.create(user=self.user, real_name='Test User', email='testuser@example.com')
        self.client.login(username='testuser', password='password')

        # Send a GET request to the view
        response = self.client.get(reverse('view_profile'))
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'view_profile.html')
        # Check that the profile is in the context
        self.assertEqual(response.context['profile'].real_name, 'Test User')
        # Check the PMA administrator status
        self.assertIn('is_pma', response.context)

    #if not a user -> redirect to create_user_profile
    def test_view_profile_without_existing_profile(self):
        self.client.login(username='testuser', password='password')
        # Send a GET request to the view
        response = self.client.get(reverse('view_profile'))
        self.assertRedirects(response, reverse('create_user_profile'))  # go here if not a user

    #user tries to click on view profile before logging in 
    def test_view_requires_login(self):
        # Send a GET request without logging in
        response = self.client.get(reverse('view_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('account_login'), response.url)    #go to login page b/c not loged in first


#Testing for logout functionality 
class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()

    def test_logout_view_logs_out_user(self):
        self.client.login(username='testuser', password='password')
        # Send a GET request to the logout view
        response = self.client.get(reverse('account_logout'))
        # Check that the user is logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/sign_out.html')

#Testing if file upload is correct
class FileUploadTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.project = Project.objects.create(title='Test Project', owner=self.user, description='Test Description')
        self.client = Client()

    #when clicking on create new project -> check if render form is correct
    def test_get_request_renders_form(self):
        self.client.login(username='testuser', password='password')
        # Send a GET request
        response = self.client.get(reverse('project_file_upload', args=[self.project.id]))
        # form is rendered -> i.e server goes to upload.html afterward 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertContains(response, 'Enter a title for your project')  #double check if we are on the correct page 

    @patch('b13project.views.upload_file_to_s3')
    def test_post_request_valid_form(self, mock_upload_file_to_s3):
        mock_upload_file_to_s3.return_value = True
        self.client.login(username='testuser', password='password')
        # test file
        file = SimpleUploadedFile("testfile.txt", b"file_content", content_type="text/plain")
        # Send a POST request with valid data
        response = self.client.post(reverse('project_file_upload', args=[self.project.id]), {
            'file': file,
            'title': 'Test File',
            'description': 'Test Description',
            'keywords': 'test, file',
        })
        # file is uploaded and in the database
        self.assertTrue(UploadedFile.objects.filter(title='Test File').exists())
        # Check that the response is a redirect to the project detail page
        self.assertRedirects(response, reverse('project_detail', args=[self.project.id]))

    def test_post_request_invalid_form_empty_title(self):
        self.client.login(username='testuser', password='password')
        # Send a POST request with missing title 
        response = self.client.post(reverse('project_file_upload', args=[self.project.id]), {
            'title': ' ',
            'description': 'Test Description',
            'keywords': 'test, file',
        })
        # Check that the form is re-rendered with an error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertContains(response, 'file', status_code=200)


    def test_post_request_invalid_form_empty_description(self):
        self.client.login(username='testuser', password='password')
        # Send a POST request with missing title 
        response = self.client.post(reverse('project_file_upload', args=[self.project.id]), {
            'title': ' ',
            'description': '',
            'keywords': 'test, file',
        })

        # Check that the form is re-rendered with an error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertContains(response, 'file', status_code=200)

    def test_post_request_invalid_form_empty_everything(self):
        self.client.login(username='testuser', password='password')
        # Send a POST request with missing title 
        response = self.client.post(reverse('project_file_upload', args=[self.project.id]), {
            'title': ' ',
            'description': '',
            'keywords': '',
        })

        # Check that the form is re-rendered with an error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertContains(response, 'file', status_code=200)
