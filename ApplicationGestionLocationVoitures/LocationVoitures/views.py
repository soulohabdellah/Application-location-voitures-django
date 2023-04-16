from django.shortcuts import render


# Admin Dashboard views

def homeds(resquest):
    return render(resquest, 'adminDashboard/home.html')


def clientds(request):
    return render(request, 'adminDashboard/client.html')
