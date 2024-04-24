from django.shortcuts import render


# Create your views here.
def home(request):
    x = 10
    y = 20
    z = [1, 2, 3, 4, 5, 6]
    names = ["suraj", "see ta", "vignette", "rani"]
    scores = [{"name": "veena", "score": 25}, {"name": "sudha", "score": 23}]
    data = {"x": x, "y": y, "z": z, "names": names, "scores": scores}
    return render(request, 'home.html', data)
