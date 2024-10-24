from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    events = Event.objects.all()  # Fetch all items from the database
    return render(request, 'index.html',{'events': events})

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