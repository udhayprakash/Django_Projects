from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

  
    request.session.setdefault('page_hits', 0)
    request.session['page_hits'] += 1
    print(f'This is request number: {request.session["page_hits"]}')

    from pprint import pprint as pp
    pp(dict(request.session))
      
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': request.session["page_hits"],

    }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class BookListView(generic.ListView):
    model = Book
    paginate_by = 2 # /catalog/books/?page=2.

    template_name = 'catalog/book_list.html'  # '<app_name>/<model>_list.html
    
    # context_object_name = 'book_list'   # your own name for the list as a template variable

    # # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war



    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk=primary_key)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')
    
#     return render(request, 'catalog/book_detail.html', context={'book': book})

# from django.shortcuts import get_object_or_404

# def book_detail_view(request, primary_key):
#     book = get_object_or_404(Book, pk=primary_key)
#     return render(request, 'catalog/book_detail.html', context={'book': book})

class BookDetailView(generic.DetailView):
    model = Book