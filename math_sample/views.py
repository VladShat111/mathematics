from django.shortcuts import render
from .models import Lesson
# Create your views here.


def base(request):

    data = Lesson.objects.all()

    context = {'data': data}
    return render(request, 'math_sample/base.html', context)




