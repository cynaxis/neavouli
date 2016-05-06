
"""
A language-aware drop-in replacement for all the slugifies of the world.

Mostly Django's.
"""


def patch():
    from django.template import defaultfilters as django_defaultfilters
    from django.utils import text as django_text
    import icu
    import slugify

    transliterate = icu.Transliterator.createInstance(
        'Greek-Latin/UNGEGN; Latin-ASCII').transliterate
    # django_text.slugify is imported as '_slugify' in django_defaultfilters,
    # which is then used by the 'slugify' template filter
    slugify.slugify = django_defaultfilters._slugify = django_text.slugify = \
        lambda value, _s=django_text.slugify, _t=transliterate: _s(_t(value))
