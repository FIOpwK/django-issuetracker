from django.shortcuts import redirect, render
from issues.models import Issue


# Create your views here.
def home_page(request):
    # TODO: fix naive solution that saves empty issues with every request to the home page
    # TODO: Support more than one issue entry
    if request.method == 'POST':
        Issue.objects.create(text=request.POST['issue_text'])
        return redirect('/')

    issues = Issue.objects.all()
    return render(request, 'home.html', {'issues': issues})
