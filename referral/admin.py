from django.contrib import admin

from .models import Campaign, Referrer, UserReferrer
from .forms import CampaignAdminForm, ReferrerInlineAdminForm


class ReferrerInine(admin.TabularInline):
    form = ReferrerInlineAdminForm
    model = Referrer
    extra = 0


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'page', 'count_referrer', 'count_users')
    prepopulated_fields = {"slug": ["name"]}

    fieldsets = [
        (None, {'fields': ['name', 'description', 'pattern', 'page', 'state']}),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ['slug', 'created', 'updated', 'updated_by', 'created_by']
        }),
    ]

    readonly_fields = ('id', 'created', 'updated', 'updated_by', 'created_by')
    radio_fields = {'state': admin.HORIZONTAL}

    form = CampaignAdminForm
    inlines = (ReferrerInine, )

    def save_form(self, request, form, change):
        f = super(CampaignAdmin, self).save_form(request, form, change)
        if not f.pk:
            f.created_by = request.user
        else:
            f.updated_by = request.user

        return f


class ReferrerAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'created', 'count_users')
    form = ReferrerInlineAdminForm


class UserReferrerAdmin(admin.ModelAdmin):
    list_display = ('user', 'referrer')
    raw_id_fields = ('user',)


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Referrer, ReferrerAdmin)
admin.site.register(UserReferrer, UserReferrerAdmin)
