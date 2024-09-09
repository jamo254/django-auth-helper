# Django Auth Helper

Django Auth Helper is a flexible authentication package for Django projects that simplifies the process of setting up user authentication. It provides a custom user model, supports login with both email and username, and integrates seamlessly with Djoser for a complete authentication API.

## Features

- Custom User model with email as the primary identifier
- Authentication using either email or username
- Integration with Djoser for out-of-the-box authentication endpoints
- Easy to install and configure

## Installation

1. Install the package using pip:

    ```bash
    pip install django-auth-helper
    ```

2. Add `django_auth_helper` and its dependencies to your `INSTALLED_APPS` in `settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'django_auth_helper',
        'rest_framework',
        'djoser',
    ]
    ```

## Configuration

1. Set the custom User model in your `settings.py`:

    ```python
    AUTH_USER_MODEL = 'django_auth_helper.User'
    ```

2. Configure the authentication backends in `settings.py`:

    ```python
    AUTHENTICATION_BACKENDS = [
        'django_auth_helper.backends.EmailOrUsernameModelBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]
    ```

3. Include the URLs in your main `urls.py`:

    ```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('django_auth_helper.urls')),
    ]
    ```

4. Configure Djoser in `settings.py`:

    ```python
    DJOSER = {
        'SERIALIZERS': {
            'user_create': 'django_auth_helper.serializers.UserCreateSerializer',
        },
    }
    ```

5. (Optional) Configure JWT settings if you're using JWT authentication:

    ```python
    from datetime import timedelta

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }
    ```

## Usage

Once installed and configured, Django Auth Helper provides several endpoints for authentication:

- `/auth/users/` - User registration
- `/auth/jwt/create/` - Obtain JWT token
- `/auth/jwt/refresh/` - Refresh JWT token
- `/auth/users/me/` - Retrieve/update authenticated user

### Example: User Registration

To register a new user, send a POST request to `/auth/users/`:

```python
import requests

url = 'http://your-domain.com/auth/users/'
data = {
    'email': 'user@example.com',
    'username': 'newuser',
    'password': 'securepassword123'
}

response = requests.post(url, data=data)
print(response.json())
