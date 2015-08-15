from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Welcome to the first page of itinerary Builder %s.</body></html>" % now
    return HttpResponse(html)
