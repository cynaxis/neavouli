# If you need to define any forms specific to this country's site, put
# those definitions here.

from __future__ import unicode_literals

from django import forms

from popolo.models import Area


class DistrictForm(forms.Form):
    district = forms.ChoiceField(
        label='Επέλεξε εκλογική περιφέρεια',
        choices=sorted(((area.identifier, area.name)
                        for area in Area.objects.all()), key=lambda i: i[1]))
