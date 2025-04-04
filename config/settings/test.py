from .default import *  # noqa: E402, F403, F401

# speed up tests
# https://docs.djangoproject.com/en/dev/topics/testing/overview/#speeding-up-the-tests
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
