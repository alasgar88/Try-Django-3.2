from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
import os

from trydjango.settings import SECRET_KEY


class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        # settings.SECRET_KEY
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY, "$w*6lq=7f4=#a$lm*nzg0asy0_fv$ri27s#ec0soh#w_5n$==r")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Bad Secret key{e.messages}"
            self.fail(msg)
