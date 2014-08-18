import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from users.models import Disc

def _create_disc(color, column, row):
    """
    Creates a new Disc for testing purposes.
    """
    return Disc.objects.create(color=color, column=column, row=row)

class TestAPIView(TestCase):

    def test_get_shows_empty_array_when_no_discs(self):
        # Index page shows a message when there is no polls.
        response = self.client.get(reverse("api:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "[]")

    def test_get_shows_discs(self):
        # Index page shows a message when there is no polls.
        _create_disc("r", 0, 0)
        _create_disc("y", 0, 1)

        response = self.client.get(reverse("api:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "r")
        self.assertContains(response, "y")
