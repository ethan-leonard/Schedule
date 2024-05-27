from django.http import JsonResponse
from .models import Staff
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'schedule.html')

def staff_availability(request):
    staff_members = Staff.objects.all()
    data = []

    for member in staff_members:
        availabilities = member.availabilities.all()
        availabilities_list = [str(a) for a in availabilities]
        data.append({
            'name': member.name,
            'role': member.get_role_display(),
            'availabilities': availabilities_list,
        })
    print(data)
    return JsonResponse(data, safe=False)