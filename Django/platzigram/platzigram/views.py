"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
from django.http import JsonResponse
import json


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    """Hi."""
    numbers = request.GET['numbers']
    numbers_1 = list(numbers.split(","))
    numbers_1 = list(map(int,numbers_1))
    numbers_1.sort()
    return JsonResponse(numbers_1, safe=False)


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')

def bye(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}!   Welcome to Platzigram'.format(name)
    return(HttpResponse(message))
