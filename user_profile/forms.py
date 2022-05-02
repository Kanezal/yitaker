from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'city', 'other_socnet', 'career',
            'interests', 'favorite_musics',
            'favorite_movies', 'favorite_movies',
            'favorite_TVshows', 'favorite_books',
            'favorite_games', 'favorite_quotes',
            'status', 'about_me', 'life_position',
            'political_preferences', 'world_outlook',
            'world_outlook', 'main_in_life', 
            'attitude_to_smoking', 'attitude_to_alcohol',
            'inspires',
        ]