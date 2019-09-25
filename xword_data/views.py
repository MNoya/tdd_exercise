from django.shortcuts import render


def drill(request):
    return render(request, 'drill.html', {})


def answer(request, clue_id):
    return render(request, 'answer.html', {})
