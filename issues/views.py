from django.shortcuts import redirect, render
from issues.models import Issue


# Create your views here.
def home_page(request):

    if request.method == 'POST':
        Issue.objects.create(text=request.POST['issue_text'])
        return redirect('/issues/the-only-issue/')
    return render(request, 'home.html')


def view_issues(request):
    issues = Issue.objects.all()
    return render(request, 'issues.html', {'issues': issues})
