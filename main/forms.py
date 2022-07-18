from django import forms

from .models import ShortLink


class ShortLinkForm(forms.ModelForm):
    """ форма для сокращенния ссылки """

    class Meta:
        model = ShortLink
        fields = ['full_link']
