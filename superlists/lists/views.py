from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
from lists.scrape_user import scrape
from lists.kball import kmfunc

def home_page(request):
    roll_no = ''
    course_list = []
    recommended_courses = []
    items = []
    if request.method == 'POST':
        roll_no = int(request.POST['item_text'])
        course_list = scrape(roll_no)

        # Removing the database logic for improved latency
        """
        for course in course_list:
            Item.objects.create(text=course)
        """

        recommended_courses = kmfunc(course_list[1:], roll_no, 25)

        return render(request, 'home.html', {
            'recommended_courses': recommended_courses,
            'items': course_list[len(course_list)-10 : ],
            'roll_no': roll_no
            })

    return render(request, 'home.html', {
        'recommended_courses': recommended_courses,
        'items': course_list[len(course_list)-10 : ],
        'roll_no': roll_no
        })
