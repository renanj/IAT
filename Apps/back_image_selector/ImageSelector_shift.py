# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ImageSelector_shift(Component):
    """An ImageSelector_shift component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- selectedImages (list; optional): The value displayed in the input.
- images (dict; required): The images array. images has the following type: list of dicts containing keys 'src', 'thumbnail', 'srcset', 'caption', 'thumbnailWidth', 'thumbnailHeight', 'isSelected', 'customdata'.
Those keys have the following types:
  - src (string; required)
  - thumbnail (string; required)
  - srcset (list; optional)
  - caption (string | dash component; optional)
  - thumbnailWidth (number; required)
  - thumbnailHeight (number; required)
  - isSelected (boolean; optional)
  - customdata (number; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, selectedImages=Component.UNDEFINED, images=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'selectedImages', 'images']
        self._type = 'ImageSelector_shift'
        self._namespace = 'image_selector'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'selectedImages', 'images']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['images']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ImageSelector_shift, self).__init__(**args)
