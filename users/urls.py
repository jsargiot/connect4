from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns("",
    url(r"^$", views.index, name="index"),
    # Url for each player
    url(r"^(?P<player_id>\d+)/$", views.user, name="user"),
)
