from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    num_of_words = len(user_text.split())
    return render(request, 'reverse.html', {
        'usertext': user_text,
        'reverse': reverse_text,
        'num_of_words': num_of_words,
        })
