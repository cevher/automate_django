from django.apps import apps

def get_all_custom_models():
    """
    Returns a list of all custom models in the project.
    Custom models are those that are not part of Django's built-in models.
    """
    default_models = ['ContentType', 'Permission', 'Session', 'LogEntry', 'Group', 'User', 'Upload']
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            # Exclude models that are not custom (e.g., those in django.contrib)
            custom_models.append(model.__name__)
    return custom_models