from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns("",
    # Main API url, will receive both GET and POST.
    url(r"^disc/$", views.disc, name="index"),
)
