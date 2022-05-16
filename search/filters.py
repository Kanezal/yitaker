import django_filters
from user_profile.models import Profile
from django_filters import CharFilter

class ProfileFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='user__last_name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    other_socnet = CharFilter(field_name='other_socnet', lookup_expr='icontains')
    career = CharFilter(field_name='career', lookup_expr='icontains')
    interests = CharFilter(field_name='interests', lookup_expr='icontains')
    favorite_musics = CharFilter(field_name='favorite_musics', lookup_expr='icontains')
    favorite_movies = CharFilter(field_name='favorite_movies', lookup_expr='icontains')
    favorite_TVshows = CharFilter(field_name='favorite_TVshows', lookup_expr='icontains')
    favorite_books = CharFilter(field_name='favorite_books', lookup_expr='icontains')
    favorite_games = CharFilter(field_name='favorite_games', lookup_expr='icontains')
    favorite_quotes = CharFilter(field_name='favorite_quotes', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='icontains')
    about_me = CharFilter(field_name='about_me', lookup_expr='icontains')
    life_position = CharFilter(field_name='life_position', lookup_expr='icontains')
    political_preferences = CharFilter(field_name='political_preferences', lookup_expr='icontains')
    world_outlook = CharFilter(field_name='world_outlook', lookup_expr='icontains')
    main_in_life = CharFilter(field_name='main_in_life', lookup_expr='icontains')
    main_in_people = CharFilter(field_name='main_in_people', lookup_expr='icontains')
    attitude_to_smoking = CharFilter(field_name='attitude_to_smoking', lookup_expr='icontains')
    attitude_to_alcohol = CharFilter(field_name='attitude_to_alcohol', lookup_expr='icontains')
    inspires = CharFilter(field_name='inspires', lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'other_socnet', 'career', 'interests', 'favorite_musics', 'favorite_movies',
                  'favorite_TVshows', 'favorite_books', 'favorite_games', 'favorite_quotes', 'status',
                 'about_me', 'life_position', 'political_preferences', 'world_outlook', 'main_in_life',
                 'main_in_people', 'attitude_to_smoking', 'attitude_to_alcohol', 'inspires']
        exclude = ['user', 'img', 'rating', 'img_confirmation']


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
