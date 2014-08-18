from django.db import models
from django.db.models import Max

# Create your models here.
class Disc(models.Model):
    """
    An object of this class represents the disc that is inserted in the grid.
    """
    color = models.CharField(max_length=1)
    column = models.IntegerField("column")
    row = models.IntegerField("row")


def calculate_row_available(column):
    """
    Calculate the next row available of this column. Return -1 if no row
    is available.
    """
    res = Disc.objects.filter(column__exact=column).aggregate(Max('row'))
    if 'row__max' in res:
        if res['row__max'] is None:
            return 0
        if res['row__max'] < 5:
            return res['row__max'] + 1
    return -1
