from django.shortcuts import render, redirect
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')

        registration = Register(name=name, gender=gender,
                                email=email, address=address)
        registration.save()

        # Redirect to the record page after successful registration
        return redirect('record')

    return render(request, 'registration.html')


@csrf_exempt
def record(request):
    registrations = Register.objects.all()
    return render(request, 'record.html', {'registrations': registrations})


@csrf_exempt
def delete_registration(request, record_id):
    registration = get_object_or_404(Register, id=record_id)

    if request.method == 'DELETE':
        registration.delete()
        return JsonResponse({'message': 'Record deleted successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt
def edit_registration(request, record_id):
    registration = get_object_or_404(Register, id=record_id)

    if request.method == 'POST':
        registration.name = request.POST.get('name')
        registration.gender = request.POST.get('gender')
        registration.email = request.POST.get('email')
        registration.address = request.POST.get('address')
        registration.save()

        # Redirect to the record page after successful editing
        return redirect('record')

    return render(request, 'edit_registration.html', {'registration': registration})
