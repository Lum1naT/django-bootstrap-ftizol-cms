from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse


from .forms import WorkerAuthMailForm
from .models import ft_Worker, ft_Upcoming_Event


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
                if(worker_found.password == form_password):
                    # Username ok, password matches :)
                    # set sessions
                    request.session['username'] = form_username
                    request.session['id'] = worker_found.id
                    return redirect('upcoming_events')

                # Username ok, password does not match!
                return HttpResponse("Your username and password didn't match.")

            else:
                form = WorkerAuthMailForm()
                return render(request, 'main/login.html.twig', {'form': form, 'worker_not_found': form_username})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkerAuthMailForm()

    return render(request, 'main/login.html.twig', {'form': form})


def my_account(request):
    cookie_username = request.session['username']
    worker_found = get_object_or_404(ft_Worker, username=cookie_username)
    worker_username = worker_found.username
    return render(request, 'main/worker_account.html.twig', {'title': str(worker_found.id) + worker_username + ' - Můj Účet', 'worker': worker_found})


def find_worker(request, worker_id):
    worker_found = get_object_or_404(ft_Worker, id=worker_id)
    worker_username = worker_found.username
    return render(request, 'main/worker_detail.html.twig', {'title': 'Účet uživatele - ' + worker_username, 'worker': worker_found})


def find_all_workers(request):
    result = ""
    found_workers = ft_Worker.get.all()
    for worker in found_workers:
        worker_username = worker.username
    return render(request, 'main/worker_account.html.twig', {'title': + 'workers list', 'workers': found_workers})


def frogot_password(request):
    cookie_username = request.session['username']
    username = cookie_username
    return render(request, 'main/frogot_password.html.twig', {'title': 'Zapomenuté heslo?', 'username': username})


def upcoming_events(request):
    all_upcoming_events = ft_Upcoming_Event.objects.all().order_by('start_date')

   # print(x.strftime("%A"))

    return render(request, 'main/upcoming_events.html.twig', {'title': 'Nadcházející akce', 'events': all_upcoming_events})


def upcoming_event_detail(request, event_id):
    event_found = ft_Upcoming_Event.objects.get(id=event_id)

    all_upcoming_events = ft_Upcoming_Event.objects.all()

    if(event_found):
        # OK
        session_id = request.session['id']
        return render(request, 'main/upcoming_event_detail.html.twig', {'title': 'Nadcházející akce ', 'event': event_found, 'session_id': session_id, 'upcoming_events': all_upcoming_events})
    else:
        # not found
        return HttpResponse("Bohužel jsme takovou akci nenašli :(")


def event_signup(request):

    if request.method == 'POST':

        event_id = request.POST.get('event_id', '')
        session_id = request.POST.get('session_id', '')
        ready = request.POST.get('ready', '')

        worker_found = get_object_or_404(ft_Worker, id=int(session_id))
        event_found = get_object_or_404(ft_Upcoming_Event, id=int(event_id))

        if(worker_found and event_found):
            # OK
            worker = worker_found
            event = event_found
            if(ready == "true"):
                event.workers_ready.add(worker)
            elif (ready == "false"):
                event.workers_ready.remove(worker)

            event.save()

            return redirect(reverse('upcoming_event_detail', kwargs={"event_id": event_found.id}))

    else:
        return redirect('upcoming_events')

    all_upcoming_events = ft_Upcoming_Event.objects.all()

    if(event_found):
        # OK
        session_id = request.session['id']
        return render(request, 'main/upcoming_event_detail.html.twig', {'title': str(event_id) + 'Na ' + str(session_id) + 'dcházející akce ', 'event': event_found, 'session_id': session_id, 'upcoming_events': all_upcoming_events})
    else:
        # not found
        return HttpResponse("Bohužel jsme takovou akci nenašli :(")
