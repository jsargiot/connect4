from django.shortcuts import render

# Create your views here.
def index(request):
    """Shows a simple page to redirect to the game."""
    return render(request, "users/index.html")

def user(request, player_id):
    """
    View for each user. This is the main game screen.
    """
    color = "y"
    if player_id == "1":
        color = "r"
    return render(request, "users/player.html", {
        'player_id': player_id,
        'player_color': color,
        })
