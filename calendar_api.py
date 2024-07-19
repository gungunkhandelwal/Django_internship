import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, time
import pytz


SCOPES = ["https://www.googleapis.com/auth/calendar"]


def combine_date_time(date_field, time_field, timezone_str='UTC'):
    # Combine date and time into a naive datetime object
    naive_datetime = datetime.combine(date_field, time_field)
    
    # Localize the naive datetime object to the specified timezone
    timezone = pytz.timezone(timezone_str)
    localized_datetime = timezone.localize(naive_datetime)

    # Convert to ISO 8601 format with timezone offset
    iso_format_datetime = localized_datetime.isoformat()

    return iso_format_datetime


def get_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def create_event(service, doctor_email, speciality, date, start_time, end_time,calendar_id='primary'):
    try:
        start_datetime =combine_date_time(date,start_time, 'Asia/Kolkata')
        end_datetime = combine_date_time(date,end_time, 'Asia/Kolkata')
        event = {
            'summary': f'Appointment for {speciality}',
            'location': 'Metro Hospital, Sector-11, Noida',
            'description': 'Appointment for health check-up.',
            'colorId': 6,
            'start': {
                'dateTime':start_datetime,
            },
            'end': {
                'dateTime': end_datetime,
            },
            'attendees': [
                {'email': doctor_email},
            ],
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
    except HttpError as error:
        print(f'An error occurred: {error}')
        