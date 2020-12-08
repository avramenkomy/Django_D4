from django.shortcuts import render
from p_library.models import Author, Book, Publisher
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def publish_list(request):
    template = loader.get_template('publish_list.html')
    pub_list = Publisher.objects.all()
    pub_data = {}
    for pub in pub_list:
        pub_data['%s' % pub.pub_name] = [book.title for book in Book.objects.filter(publisher=pub.id)] # Book.objects.all().filter(publisher=pub.id) #
    print(pub_data)
    biblio_data = {
        'pub_data': pub_data,
    }
    return HttpResponse(template.render(biblio_data))

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')