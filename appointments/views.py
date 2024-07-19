from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import CustomUser
from . forms import AppointmentForm
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from calendar_api import create_event,get_credentials
from googleapiclient.discovery import build

@login_required(login_url='/')
def doctor_list(request):
    doctors=CustomUser.objects.filter(is_doctor=True)
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

            print(appointment.speciality)
            print(appointment.date)
            print(appointment.start_time)
            print(appointment.end_time)

            creds = get_credentials()
            service = build("calendar", "v3", credentials=creds)
            create_event(service,doctor_email=doctor.email,speciality= appointment.speciality, 
                          date=appointment.date, start_time=appointment.start_time, 
                          end_time=appointment.end_time)
            print('Event created')
            messages.info(request,"Appointment Booked and Confirmation Done !!")
            return redirect('appointment_details', appointment_id=appointment.id)
    else:
        form=AppointmentForm()
    return render(request,'book_appointment.html',{'form':form,'doctor':doctor})
        
@login_required(login_url='/')
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointments, id=appointment_id)
    return render(request, 'appointment_details.html', {'appointment': appointment})

def appointment_list(request):
 doctor = request.user
 appointments = Appointments.objects.filter(doctor=doctor)
    
    # Accessing patient names
 for appointment in appointments:
        patient_name = f"{appointment.patient.first_name} {appointment.patient.last_name}"
    
 return render(request, 'appointment_list.html', {'appointments': appointments})