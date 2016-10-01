from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
from lists.scrape_user import scrape
from lists.dummy import return_list
from lists.ml2 import kmfunc

def home_page(request):
    new_item_text = ''
    course_list = []
    temp_list = []
    items = []
    if request.method == 'POST':
        new_item_text = int(request.POST['item_text'])
        course_list = scrape(new_item_text)
        # for course in course_list:
            # Item.objects.create(text=course)

        # Item.objects.create(text=(scrape(new_item_text)))
        # items = []
        # items = scrape(new_item_text)
        # temp_list = kmfunc(course_list[1:], 14658, 12)
        # return redirect('/')

        # items = Item.objects.all()
        items2 = ['ART105A', 'ART106A', 'CHM101A', 'CHM102A', 'COM200', 'EE200A',
            'EE210A', 'EE250A', 'ESC101A', 'ESC201A', 'ESO201A', 'ESO203A',
            'LIF101A', 'MSO201A', 'MSO202A', 'MSO203B', 'MTH101A', 'MTH102A',
            'PE101A', 'PE102A', 'PHY101A', 'PHY102A', 'PHY103A', 'TA101A',
            'TA201A', 'TA202A']
        temp_list = kmfunc(course_list[1:], new_item_text, 12)
        # temp_list = return_list()
        return render(request, 'home.html', {
            'temp_list': temp_list,
            # 'items': items
            'items': course_list[1:]
            })

    return render(request, 'home.html', {
        'temp_list': temp_list,
        'items': items
        })
