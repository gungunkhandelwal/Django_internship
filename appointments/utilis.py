from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# def create_google_calendar_event(doctor_email, speciality, date, start_time, end_time):
#     SCOPES = ['https://www.googleapis.com/auth/calendar']
#     SERVICE_ACCOUNT_FILE = 'credentls.json'
    
#     try:
#         credentials = service_account.Credentials.from_service_account_file(
#             SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
#         service = build('calendar', 'v3', credentials=credentials)
        
#         # Format date and time properly
#         start_datetime = datetime.strptime(f'{date}T{start_time}', '%Y-%m-%dT%H:%M')
#         end_datetime = datetime.strptime(f'{date}T{end_time}', '%Y-%m-%dT%H:%M')
        
#         event = {
#             'summary': f'Appointment for {speciality}',
#             'start': {
#                 'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
#                 'timeZone': 'Asia/Kolkata', 
#             },
#             'end': {
#                 'dateTime': end_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
#                 'timeZone': 'Asia/Kolkata',
#             },
#             'attendees': [
#                 {'email': doctor_email},
#             ],
#         }
        
#         event = service.events().insert(calendarId='primary', body=event).execute()
#         print('Event created: %s' % (event.get('htmlLink')))
#         return event
    
#     except Exception as e:
#         print(f'Error creating event: {e}')
#         return None

def create_google_calendar_event():
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    credentials = service_account.Credentials.from_service_account_file(
            'credentails.json', scopes=SCOPES)
    print(credentials)