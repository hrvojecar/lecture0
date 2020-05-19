import random
from django.http import HttpResponse

def give_random():

    ra = random.random()
    return HttpResponse(ra)
    
give_random()
