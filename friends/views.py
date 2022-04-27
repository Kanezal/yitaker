from django.shortcuts import render, redirect

# Create your views here.
from friends.models import Friends

def my_friends(request):
    f1 = Friends.objects.filter(user1=request.user, user2_confirmation=True)
    f2 = Friends.objects.filter(user2=request.user)
    ctx = {
        'f1': f1,
        'f2': f2,
    }
    return render(request, 'friends.html', ctx)



def add_to_friends(request, id):
    f = Friends.objects.all()
    if f.user1 != None:
        f.user1 = request.user
        f.friend = id
    else:
        f.user2 = request.user
        f.user2_confirmation = True

    f.save()
    return redirect('profile')


