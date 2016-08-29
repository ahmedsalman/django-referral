from . import settings
from .models import Referrer


class ReferrerMiddleware():
    def process_request(self, request):
        if settings.GET_PARAMETER in request.GET:
            referrer = None
            referrer_name = request.GET.get(settings.GET_PARAMETER, '').strip()
            if not referrer_name:
                return
            try:
                if settings.CASE_SENSITIVE:
                    referrer = Referrer.objects.filter(name=referrer_name)
                else:
                    referrer = Referrer.objects.filter(name__iexact=referrer_name)

                if referrer:
                    referrer = referrer[0]
                #else:
                #    if settings.AUTO_CREATE:
                #        referrer = Referrer(name=referrer_name)
                #        referrer.save()
            finally:
                if referrer:
                    request.session[settings.SESSION_KEY] = referrer.pk
