from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_issue_text': request.POST.get('issue_text', ''),
    })
