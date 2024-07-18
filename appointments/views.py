from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import CustomUser
from . forms import AppointmentForm
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def doctor_list(request):
    doctors=CustomUser.objects.filter(is_doctor=True)
    print(doctors)
    return render(request,'doctor_list.html',{'doctors':doctors})


@login_required(login_url='/')
def book_appointment(request,doctor_id):
    doctor=get_object_or_404(CustomUser,id=doctor_id)
    if request.method == "POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            appointment=form.save(commit=False)
            appointment.patient=request.user
            appointment.doctor=doctor
            appointment.save()
            messages.info(request,"Appointment Booked Successfully !!")
            return redirect('appointment_details', appointment_id=appointment.id)
    else:
        form=AppointmentForm()
    return render(request,'book_appointment.html',{'form':form,'doctor':doctor})
        
@login_required(login_url='/')
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointments, id=appointment_id)
    return render(request, 'appointment_details.html', {'appointment': appointment})


