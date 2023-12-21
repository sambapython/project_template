from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from app1.models import Cricketers


# models test
class CricketersTest(TestCase):

    def create_Cricketers(self, title="only a test", body="yes, this is only a test"):
        return Cricketers.objects.create(name=title, image_path=body, age=7)

    def test_Cricketers_creation(self):
        w = self.create_Cricketers()
        self.assertTrue(isinstance(w, Cricketers))
      