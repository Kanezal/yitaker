# Yitaker Social Network

A Django-based social networking platform with rich features for user interaction and content sharing.

## Features

- User Authentication & Profiles
- News Feed System
- Private Messaging
- Friend Management
- Community/Group System 
- Search Functionality
- Profile Rating System
- Image Upload Support

## Technical Stack

- Python 3.x
- Django 4.x
- PostgreSQL
- Django REST Framework
- Bootstrap 5
- Django Filters

## Project Structure

The application is divided into several Django apps:

- `user_profile`: User profiles and settings
- `messenger`: Private messaging system
- `news`: News feed and posts
- `friends`: Friend relationships
- `community`: Group/community management
- `search`: Search functionality
- `api`: REST API endpoints
- `registration`: User authentication
- `main`: Core functionality

### user_profile
- Profile management system
- Custom user profile model extending Django's User
- Profile rating calculation
- Image handling with ResizedImageField
- Fields for personal info, interests, and preferences
- Profile editing and viewing functionality

### messenger
- Private messaging system between users
- Chat model for 1-on-1 conversations
- Group chat capabilities
- Message model with read status tracking
- Real-time chat interface
- Chat user management system

### news
- News feed system
- Post creation and management
- Like system implementation
- Image attachment support
- News filtering by friends/communities
- Timestamp-based ordering

### friends
- Bidirectional friendship system
- Friend request handling
- Request confirmation workflow
- Friend status tracking
- API endpoints for friend operations:
  - Add friend
  - Accept request
  - Delete friend
  - Check friendship status

### community
- Group/community creation and management
- Community membership tracking
- Community posts and updates
- Member management system
- Community-specific news feed
- Community roles and permissions
- Community search and discovery

### search
- Advanced search functionality
- User search
- Community search
- News/posts search
- Profile filtering system
- Search result serialization
- Filter-based query system

### registration
- Custom user registration system
- Login/logout functionality 
- Profile creation on registration
- Form validation
- Authentication decorators
- Success/error message handling

### api
- REST API implementation
- Friend management endpoints:
  - GET /api/is-friend/{id}/ 
  - GET /api/add-friend/{id}/
  - GET /api/accept-friend/{id}/
  - GET /api/delete-friend/{id}/
- Response serialization
- API authentication
- Status code handling

### main
- Core application views
- Base context processors
- Navigation management
- Static page rendering
- About/info pages
- Future plans section

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure PostgreSQL settings in `settings.py`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## Security

- CSRF protection enabled
- Authentication required for most views
- PostgreSQL for secure data storage

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Open pull request

## License

MIT License