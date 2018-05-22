from django.shortcuts import render

# creating a function to take a request and return a function to render the template blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
