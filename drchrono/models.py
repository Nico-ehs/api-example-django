from django.db import models
from social_django.models import UserSocialAuth
import datetime
import requests

def get_header_token():
    oauth_provider = UserSocialAuth.objects.get(provider='drchrono')
    access_token = oauth_provider.extra_data['access_token']
    return {'Authorization': 'Bearer %s' % access_token,}

def api_get_request(url, params):
    return requests.get(url,params=params, headers=get_header_token())

def api_post_request(url, params):
    return requests.post(url,params=params, headers=get_header_token())

def api_update_request(url, params):
    return requests.get(url,params=params, headers=get_header_token())

class AppointmentApi():
    def appointments_today(self):
        return api_get_request('https://drchrono.com/api/appointments', {'date' : datetime.date.today().isoformat()})

    def appointments_this_year(self):
        return api_get_request('https://drchrono.com/api/appointments', {'since' : datetime.date.today().isoformat()})

    def set_status(self,id, new_status):
        return api_update_request('https://drchrono.com/api/appointments/'+str(id), {'status':new_status} )
    def get_patient_info(self,paitent_id):
        return 1

    def update_patient_info(self, paitent_id, new_info):
        return api_update_request('https://drchrono.com/api/paitents/'+str(paitent_id), new_info)

# Add your models here

class Appointment(models.Model):

    drchrono_id = models.IntField(null=False)
    paitent_drchron_id=models.IntField(null=False)
    status=models.CharField(max_length=10)
    time_checked_in = models.DateTimeField(blank=True)
    time_seen = models.DateTimeField(blank=True)
    wait_time = models.IntField()
