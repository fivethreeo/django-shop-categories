from django.conf import settings
from django.core import exceptions

def get_model_string(model_name, setting_format='SHOP_%s_MODEL', fallback_format='shop.%s'):
    """
    Returns the model string notation Django uses for lazily loaded ForeignKeys
    (eg 'auth.User') to prevent circular imports.

    This is needed to allow our crazy custom model usage.
    """
    setting_name = setting_format % model_name.upper().replace('_', '')
    class_path = getattr(settings, setting_name, None)
        
    if not class_path:
        return fallback_format % model_name
    elif isinstance(class_path, basestring):
        parts = class_path.split('.')
        try:
            index = parts.index('models') - 1
        except ValueError, e:
            raise exceptions.ImproperlyConfigured(CLASS_PATH_ERROR % (setting_name, setting_name))
        app_label, model_name = parts[index], parts[-1]
    else:
        try:
            class_path, app_label = class_path
            model_name = class_path.split('.')[-1]
        except:
            raise exceptions.ImproperlyConfigured(CLASS_PATH_ERROR % (setting_name, setting_name))

    return "%s.%s" % (app_label, model_name)
    
def get_category_model_string(model_name):
    return get_model_string(model_name, setting_format='CATEGORYPRODUCT_%s_MODEL', fallback_format='category_product.%s')