from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse


from .forms import WorkerAuthMailForm
from .models import ft_Worker


# Create your views here.

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkerAuthMailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            form_username = data["username"]
            form_password = data["password"]
            worker_found = get_object_or_404(ft_Worker, username=form_username)

            if(worker_found):
                # Username ok, password does not match!
                return HttpResponse("Your username and password didn't match.")

            elif(worker_found.password == form_password):
                # Username ok, password matches :)
                pass
            else:
                form = WorkerAuthMailForm()
                return render(request, 'main/login.html.twig', {'form': form})

            # redirect to a new URL:
            return redirect('admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkerAuthMailForm()

    return render(request, 'main/login.html.twig', {'form': form})
