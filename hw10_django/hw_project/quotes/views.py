from django import db
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

# from Django1-main.quotes import TagForm

# Create your views here.
from .utils import get_mongodb



def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context= {'quotes': quotes_on_page})

# def tag(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='quotes:main')
#         else:
#             return render(request, 'quotes/tag.html', {'form': form})

#     return render(request, 'quotes/tag.html', {'form': TagForm()})

#quotes = db.quotes.find()


#for quote in quotes:
    #print(quote.tags)
