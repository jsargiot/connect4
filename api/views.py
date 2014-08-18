from django.shortcuts import render
from django.http import HttpResponse
import json

from users.models import Disc, calculate_row_available

# Create your views here.
def disc(request):
    """
    This view will handle the GET and POST of the discs.
    """
    if request.method == 'GET':
        return _handle_get(request)
    if request.method == 'POST':
        return _handle_post(request)

def _handle_get(request):
    """Return all the discs in the game."""
    objects = Disc.objects.all()
    result = []
    for o in objects:
        result.append({
            "color": o.color,
            "column": o.column,
            "row": o.row,
            })
    return HttpResponse(json.dumps(result))

def _handle_post(request):
    """ 
    Handles the creation of a new disc, in the game it means an user has
    inserted the disc in a column.
    """
    try:
        color = request.POST.get("color")
        column = request.POST.get("column")

        row = calculate_row_available(column)
        if row >= 0:
            d = Disc(color=color, column=column, row=row)
            d.save()
            return HttpResponse(json.dumps({
                "color": d.color,
                "column": d.column,
                "row": d.row,
            }))
    except Exception as e:
        return HttpResponse('{"error_message": "' + repr(e) + '"')

