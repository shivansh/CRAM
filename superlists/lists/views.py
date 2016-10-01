from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
from lists.scrape_user import scrape

def home_page(request):
    new_item_text = ''
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        course_list = scrape(new_item_text)
        for course in course_list:
            Item.objects.create(text=course)
        # Item.objects.create(text=(scrape(new_item_text)))
        # items = []
        # items = scrape(new_item_text)
        return redirect('/')

    items = Item.objects.all()

    return render(request, 'home.html', {
        'items': items
        })
