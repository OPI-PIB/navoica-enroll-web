from django.utils.translation import ugettext_lazy as _

STATUSES_OPTIONS = {
    'employed': [
        _("A person working in the government administration"),
        _("A person working in local government administration"),
        _("Other"),
        _("A person works in MSME"),
        _("A person working in a non-governmental administration"),
        _("A self-employed person"),
        _("A person working in a large enterprise")
    ],
    'registered': [
        _("Long-term unemployed person"),
        _("Other")
    ],
    'unregistered': [
        _("Long-term unemployed person"),
        _("Other")
    ],
    'looking': [
        _("Learning"),
        _("A person not participating in education or training"),
        _("Other")
    ]

}
