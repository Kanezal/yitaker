from django import forms
from .models import Profile
class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=['%d/%m/%Y'], label='Дата рождения (дд/мм/гггг)', required=False)
    class Meta:
        model = Profile
        fields = [
            'img', 'gender', 'birthday', 'city',
            'other_socnet', 'career',
            'interests', 'favorite_musics',
            'favorite_movies', 'favorite_movies',
            'favorite_TVshows', 'favorite_books',
            'favorite_games', 'favorite_quotes',
            'status', 'about_me', 'life_position',
            'political_preferences', 'world_outlook',
            'world_outlook', 'main_in_life', 'main_in_people',
            'attitude_to_smoking', 'attitude_to_alcohol',
            'inspires',
        ]
        # fields = '__all__'
