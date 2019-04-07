from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    splitted_word = text.split()
    total = "".join(splitted_word)
    word = []

    for i in splitted_word:
        if i + ":" + str(splitted_word.count(i)) in word:
            pass
        else:
            word.append(i + ":" + str(splitted_word.count(i)))
        

    return render(request, 'result.html', {
        "length": len(splitted_word),
        "text": text,
        "word": word
    })