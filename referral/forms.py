import datetime
import autocomplete_light

from django import forms
from django.utils.translation import ugettext_lazy as _
from referral.models import Campaign, Referrer

MEDIUM_TYPES = (
    ('', _('')),
    (0, _('Email')),
    (1, _('On Site')),
)


class CampaignAdminForm(forms.ModelForm):

    class Meta(object):
        model = Campaign
        widgets = {
            'created_by': autocomplete_light.ChoiceWidget('UserAdminAutocomplete'),
            'updated_by': autocomplete_light.ChoiceWidget('UserAdminAutocomplete'),
        }


class ReferrerInlineAdminForm(forms.ModelForm):

    class Meta(object):
        model = Referrer
        widgets = {
            'created_by': autocomplete_light.ChoiceWidget('UserAdminAutocomplete'),
            'updated_by': autocomplete_light.ChoiceWidget('UserAdminAutocomplete'),
        }