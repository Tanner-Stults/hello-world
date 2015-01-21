import autocomplete_light
from models import Education

# This will generate a PersonAutocomplete class
autocomplete_light.register(Education,
    # Just like in ModelAdmin.search_fields
    search_fields=['degree'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Other model name ?',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

class DegreeAutocomplete(autocomplete_light.AutocompleteListBase):
    choices = {'Ph. D', 'BA', 'BS', 'Master\'s', 'AA'}
    autocomplete_js_attributes={'placeholder': 'degree'}

autocomplete_light.register(DegreeAutocomplete)
