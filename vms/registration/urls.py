# Django
from django.conf.urls import url

# local Django
# from administrator.views import AdministratorSignUpView
# from registration import views
from registration.views import AdministratorSignupView, VolunteerSignupView, load_cities, load_states, check_states

urlpatterns = [
    url(r'^signup_administrator/$',
        AdministratorSignupView.as_view(),
        name='signup_administrator'),
    url(r'^signup_volunteer/$',
        VolunteerSignupView.as_view(),
        name='signup_volunteer'),
    url(r'^check_states/$', check_states, name='check_states'),
    url(r'^load_cities/$', load_cities, name='load_cities'),
    url(r'^load_states/$', load_states, name='load_states'),
]

