from django.shortcuts import render
from issues.models import Issue


# Create your views here.
def home_page(request):
    # TODO: fix naive solution that saves empty issues with every request to the home page
    # TODO: Support more than one issue entry
    if request.method == 'POST':
        new_issue_text = request.POST['issue_text']
        Issue.objects.create(text=new_issue_text)
    else:
        new_issue_text = ''

    return render(request, 'home.html', {
        'new_issue_text': new_issue_text
    })
