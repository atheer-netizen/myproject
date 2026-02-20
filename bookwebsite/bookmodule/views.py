from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    name = request.GET.get("name") or "world!"
    return render(request, "index.html", {"name":name})

def index(request, val1=0):
    return HttpResponse("value1 = "+str(val1))