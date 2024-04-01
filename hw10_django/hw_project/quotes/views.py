from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author




def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page, 'paginator': paginator})


def author_quotes(request, author_name):
    author = get_object_or_404(Author, name=author_name)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_quotes.html', {'author': author, 'quotes': quotes})


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.author=request.user
            tag.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuoteForm()

    return render(request, 'quotes/quote.html', {'form': form})
# def add_quote(request):
#     tags = Tag.objects.filter(author=request.user).all()

#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             new_quote = form.save(commit=False)
#             new_quote.author=request.user
#             new_quote.save()
#             choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), author=request.user)
#             for tag in choice_tags.iterator():
#                 new_quote.tags.add(tag)

#             return redirect(to='quotes:main')
#         else:
#             return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})

#     return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})

@login_required
def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, author=request.user)
    return render(request, 'quotes/detail.html', {"quote": quote})


@login_required
def set_quote(request, quote_id):
    Quote.objects.filter(pk=quote_id, author=request.user).update(done=True)
    return redirect(to='quotes:main')


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, author=request.user).delete()
    return redirect(to='quotes:main')


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect('/')
    else:
        form = TagForm()
    return render(request, 'quotes/add_tag.html', {'form': form})

