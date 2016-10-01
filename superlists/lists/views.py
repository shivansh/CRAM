from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    print(item.text)

    # if request.method == 'POST':
        # return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
        })
