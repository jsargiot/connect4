from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "users/index.html")

def user(request, player_id):
    color = "y"
    if player_id == "1":
        color = "r"
    return render(request, "users/player.html", {
        'player_id': player_id,
        'player_color': color,
        })
