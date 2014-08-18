import datetime

from django.test import TestCase
from django.utils import timezone

from users.models import Disc, calculate_row_available

def _create_disc(color, column, row):
    """
    Creates a new Disc
    """
    return Disc.objects.create(color=color, column=column, row=row)

class TestModels(TestCase):
    
    def test_calculate_returns_zero_for_no_discs(self):
        self.assertEqual(calculate_row_available(0), 0)

    def test_calculate_returns_error_for_full_column(self):
        _create_disc("r", 0, 0)
        _create_disc("r", 0, 1)
        _create_disc("r", 0, 2)
        _create_disc("r", 0, 3)
        _create_disc("r", 0, 4)
        _create_disc("r", 0, 5)
        self.assertEqual(calculate_row_available(0), -1)
