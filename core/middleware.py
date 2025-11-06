from django.utils import translation
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Get the user's preferred language from their profile
            user_language = request.user.preferred_language
            
            # If the user has a preferred language and it's different from the current active language
            if user_language and user_language != translation.get_language():
                translation.activate(user_language)
                request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        else:
            # If user is not authenticated, use the language from the session or default
            if translation.LANGUAGE_SESSION_KEY in request.session:
                translation.activate(request.session[translation.LANGUAGE_SESSION_KEY])
            else:
                translation.activate(settings.LANGUAGE_CODE) # Fallback to default

        response = self.get_response(request)
        return response
