from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *

# Create your views here:
def index(request):
    return render(request, 'myApp/index.html')

def register(request):
    if request.method != 'POST':
        return redirect(reverse('myApp:index'))

    validation = User.objects.register(request.POST)
    if validation[0] == False:
        #errors!
        for error in validation[1]:
            messages.error(request, error)
        return redirect(reverse('myApp:index'))
    else:
        #no errors!
        messages.success(request, "Welcome, {}. You have successfully registered!".format(validation[1].name))
        request.session['user_id'] = validation[1].id
        return redirect(reverse('myApp:travels'))

def login(request):
    if request.method != 'POST':
        return redirect(reverse('myApp:index'))

    validation = User.objects.login(request.POST)
    print validation[0]
    if validation[0] == False:
        #errors!
        for error in validation[1]:
            messages.error(request, error)
        return redirect(reverse('myApp:index'))
    else:
        #no errors!
        messages.success(request, "Welcome, {}. You have successfully logged in!".format(validation[1].name))
        request.session['user_id'] = validation[1].id
        return redirect(reverse('myApp:travels'))


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have successfully logged out")
        return redirect(reverse('myApp:index'))
    else:
        messages.error(request, "You were not logged in")
        return redirect(reverse('myApp:index'))

## travel routes below!!

def travels(request):
    if not 'user_id' in request.session:
        messages.error(request, 'You must log in!')
        return redirect('myApp:index')

    myTrips = Trip.objects.filter(users__id__in=[request.session['user_id']])
    otherTrips = Trip.objects.exclude(users__id__in=[request.session['user_id']])
    context = {
        'myTrips': myTrips,
        'otherTrips': otherTrips
    }
    return render(request, 'myApp/travels.html', context)

def travels_add(request):
    if not 'user_id' in request.session:
        messages.error(request, 'You must log in!')
        return redirect('myApp:index')
    return render(request, 'myApp/travels_add.html')

def travels_destination(request, id):
    if not 'user_id' in request.session:
        messages.error(request, 'You must log in!')
        return redirect('myApp:index')

    trip = Trip.objects.get(id=id)
    otherUsers = User.objects.filter(all_trips__id__in=[trip.id]).exclude(id__in=[request.session['user_id']])

    context = {
        'trip': trip,
        'otherUsers': otherUsers
    }

    return render(request, 'myApp/travels_destination.html', context)


def trip_add(request):
    if not 'user_id' in request.session:
        messages.error(request, 'You must log in!')
        return redirect('myApp:index')
    if request.method != 'POST':
        return redirect(reverse('myApp:travels_add'))

    validation = Trip.objects.add(request.POST, request.session['user_id'])
    if validation[0] == False:
        #errors!
        for error in validation[1]:
            messages.error(request, error)
        return redirect(reverse('myApp:travels_add'))
    else:
        messages.success(request, "Your trip has been added!")
        return redirect(reverse('myApp:travels'))

def trip_join(request, id):
    if not 'user_id' in request.session:
        messages.error(request, 'You must log in!')
        return redirect('myApp:index')
    if request.method != 'GET':
        return redirect(reverse('myApp:travels'))

    validation = Trip.objects.join(id, request.session['user_id'])

    if validation == False:
        messages.error('Something went wrong :( Try again.')
    else:
        messages.success(request, "You have joined a trip to {}".format(validation.destination))


    return redirect(reverse('myApp:travels'))
