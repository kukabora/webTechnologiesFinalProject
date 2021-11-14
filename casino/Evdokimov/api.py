from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


def updateBalance(request):
    user = User.objects.get(id=int(request.POST['userId']))
    data = {
        "user": {
            "fname": user.first_name,
            "lname": user.last_name,
            "balance": user.player.balance
        },
        "balanceChange": request.POST['balanceDifference'],
        "newBalance": int(request.user.player.balance) + int(request.POST['balanceDifference'])
    }
    user.player.balance += int(request.POST['balanceDifference'])
    user.save()
    user.player.save()
    print(data)
    return JsonResponse(data=data, safe=False)
