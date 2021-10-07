
import os

ALLOWED_HOSTS = ['.heroku.com', 'kuhmasii.heroku.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = int(os.environ.get('DEBUG'))
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# RECIPIENT TARGET
RECIPIENT_ADDRESS = os.environ.get('RECIPIENT_ADDRESS')

# ACCESS TO AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = 'kuhmasii'

AWS_DEFAULT_ACL = None

AWS_LOCATION = 'static'
AWS_MEDIA_LOCATION = 'media'

STATIC_URL = 'https://%s.s3.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME,
    AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'backend_resume.storages.MediaStorage'