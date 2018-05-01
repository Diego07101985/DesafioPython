from django.utils.cache import patch_response_headers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings

import logging

logger = logging.getLogger('desafio')


class CacheMixin(object):
    cache_timeout = 0
    key_prefix = ''

    def get_cache_timeout(self):
        return self.cache_timeout
    
    def get_key_prefix(self):
        return self.key_prefix

    def dispatch(self, *args, **kwargs):
        logger.info(self.get_key_prefix())  
        return cache_page(self.get_cache_timeout(), key_prefix=self.get_key_prefix())(super(CacheMixin, self).dispatch)(*args, **kwargs)


    
