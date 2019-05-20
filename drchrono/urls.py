from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

import views


urlpatterns = [
    url(r'^setup/$', views.SetupView.as_view(), name='setup'),
    url(r'^welcome/$', views.DoctorWelcome.as_view(), name='setup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^today/$', views.TodayView.as_view(), name='today'),

    url(r'^checkin/$', views.CheckinView.as_view(), name='checkin'),
    url(r'^confirm/$', views.ConfirmView.as_view(), name='confirm'),
    path('update-info/<int:paitent_id>/', views.UpdatePatientInfo, name='update_patient_info')
    path('checkin-confirm/<int:appointment_id>/', views.CheckinConfirm, name='checkin_confirm')
    path('see-paitent/<int:appointment_id>/', views.SeePaitent name='see_paitent')
]
