import django_filters
from user_profile.models import Profile
from django_filters import CharFilter
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['username']

class ProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['img']


#class ProfileFilter(django_filters.FilterSet):
#    user = CharFilter(field_name='user', lookup_expr='icontains')
#    city = CharFilter(field_name='city', lookup_expr='icontains')
#    career = CharFilter(field_name='career', lookup_expr='icontains')
#    class Meta:
#        model = Profile
#        fields = '__all__'
#        exclude = ['img']

#        fields = [ 'city', 'other_socnet', 'career', 'interests', 'favorite_musics', 'favorite_movies',
#                   'favorite_TVshows', 'favorite_books', 'favorite_games', 'favorite_quotes', 'status',
#                  'about_me', 'life_position', 'political_preferences', 'world_outlook', 'main_in_life',
#                  'main_in_people', 'attitude_to_smoking', 'attitude_to_alcohol', 'inspires']
