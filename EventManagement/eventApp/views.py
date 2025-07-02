from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import EventForm
from .models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'events/Home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            confirm_password=request.POST.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'events/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('EventAdd')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'events/login.html',{'form':AuthenticationForm()})

@login_required
def add_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid(): 
            # Assuming you have a user logged in and you want to associate the event with them
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event added successfully.')
            return redirect('My_Events')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form' : form})
@login_required
def Event_list_view(request):
    events = Event.objects.all()  # Assuming you have a related name 'events' in your Event model
    return render(request, 'events/Event_List.html', {'events': events})

@login_required
def edit_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('My_Events')
    
     # If the user is the organizer, allow them to edit the event
     # Use the same form as in add_event_view
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully.')
            return redirect('My_Events')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/add_event.html', {'form': form, 'event': event})
@login_required
def delete_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect('My_Events')
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('My_Events')
    return render(request, 'events/delete.html', {'event': event})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def detail_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/details.html', {'event': event})