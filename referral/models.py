from django.db import models
from django.utils.translation import ugettext_lazy as _

from .compat import User
from django.conf import settings
from articles.constants import STATE_TYPES
from pages.models import Page
from people.models import UserPoints

class Campaign(models.Model):
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    name = models.CharField(_("Name"), max_length=255)
    page = models.ForeignKey(Page, verbose_name=_("Page"), related_name='campaign_pages')
    description = models.TextField(_("Description"), blank=True, null=True)
    pattern = models.CharField(_("Referrer pattern"), blank=True, max_length=255,
        help_text="All auto created referrers containing this pattern will be associated with this campaign")

    state = models.SmallIntegerField(verbose_name=_('Publish state'), choices=STATE_TYPES, default=1)

    created = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, related_name="campaign_created_by")

    updated = models.DateTimeField(verbose_name=_('Update date'), auto_now=True, editable=False)
    updated_by = models.ForeignKey(User, related_name="campaign_updated_by", null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    def count_users(self):
        count = 0
        for referrer in self.referrers.all():
            count += referrer.count_users()
        return count
    count_users.short_description = _("User count")


class Referrer(models.Model):
    name = models.CharField(_("Name"), max_length=255)                                      #user.username + pattern
    description = models.TextField(_("Description"), blank=True, null=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("Campaign"), related_name='referrers', blank=True, null=True)

    state = models.SmallIntegerField(verbose_name=_('Publish state'), choices=STATE_TYPES, default=1)

    created = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, related_name="referrer_created_by")

    updated = models.DateTimeField(verbose_name=_('Update date'), auto_now=True, editable=False)
    updated_by = models.ForeignKey(User, related_name="referrer_updated_by", null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Referrer")
        verbose_name_plural = _("Referrers")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    def count_users(self):
        return self.users.count()
    count_users.short_description = _("User count")

    #def match_campaign(self):
    #    for campaign in Campaign.objects.exclude(pattern=""):
    #        if campaign.pattern in self.name:
    #            self.campaign = campaign
    #            self.save()
    #            break

class UserReferrerManager(models.Manager):
    def apply_referrer(self, user, request):
        try:
            referrer = Referrer.objects.get(pk=request.session.pop(settings.SESSION_KEY))
        except KeyError:
            pass
        else:
            user_referrer = UserReferrer(user=user, referrer=referrer)
            user_referrer.save()

            reference_created_by = referrer.created_by
            user_point = UserPoints.objects.get(user=reference_created_by)
            user_point.points += settings.REFERRER_POINTS
            user_point.save()



class UserReferrer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), related_name='user_referrer')         #referrer receiver
    referrer = models.ForeignKey(Referrer, verbose_name=_("Referrer"), related_name='users')        #referrer sender

    objects = UserReferrerManager()

    class Meta:
        ordering = ['referrer__name']
        verbose_name = _("User Referrer")
        verbose_name_plural = _("User Referrers")

    def __unicode__(self):
        return "%s -> %s" % (self.user.username, self.referrer.name)

    def __str__(self):
        return self.__unicode__()
