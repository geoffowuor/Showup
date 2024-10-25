from django.shortcuts import render,get_object_or_404
from .models import Event

# Create your views here.
def home(request):
    events = Event.objects.all()  # Fetch all items from the database
    return render(request, 'index.html',{'events': events})

#event detail view
def event_detail(request, event_name):
    event = get_object_or_404(Event, name= event_name)
    return render(request, 'event_detail.html', {'event': event})
#search view
def search(request):
    query = request.GET.get('q', '') # Gets the search term from the query parameters
    if query:
        results = Event.objects.filter(name__icontains=query)
    else:
        results = Event.objects.none() # No search results if no query
        
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'event_search.html', context)
