from django.shortcuts import render


# Create your views here.
rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
    {'id': 4, 'name': 'Backend developers'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}

    return render(request, 'base/room.html', context)


def about(request):
    return render(request, 'base/about.html')
