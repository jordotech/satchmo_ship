from livesettings import config_register, ConfigurationGroup, PositiveIntegerValue, MultipleStringValue
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
SATCHMO_SHIP_GROUP = ConfigurationGroup(
    'satchmo_ship',  # key: internal name of the group to be created
    _('Satchmo Fulfillment Settings'),  # name: verbose name which can be automatically translated
    ordering=0  # ordering: order of group in the list (default is 1)
)

# Another example of allowing the user to select from several values
config_register(MultipleStringValue(
    SATCHMO_SHIP_GROUP,
    'USPS_SERVICES',
    description=_("USPS Services"),
    help_text=_("Which USPS services are available to ship with?"),
    choices=[
        ('usps_parcel_select', _('Parcel Select')),
        ('usps_priority_first_class', _('Priority or 1st Class')), #3day
        ('usps_priority', _('Priority')),
        ('usps_express', _('Express')),
        ('usps_first_class_intl', _('1st Class International')),
        ('usps_priority_intl', _('Priority International')),
        ('usps_express_intl', _('Express International'))
        ]))

'''
GROUND 	        Ground/Home         Delivery	Ground	Parcel Select 	Ground Basic	Regular Parcel
3DAY	        Express Saver	    3 Day Select	Priority or 1st Class	Ground Early	Expedited Parcel
2DAY	        2Day	            2nd Day Air	Priority	Priority Noon	Priority
2DAY_EARLY	    2Day AM	            2nd Day Air AM	Express	Priority 2nd Day	Priority
1DAY	        Standard            Overnight	Next Day Air Saver	Express	Priority Basic	Xpresspost
1DAY_EARLY	    Priority            Overnight	Next Day Air	Express	Priority Early	Xpresspost
1DAY_MORNING	First               Overnight	Next Day Air Early A.M.	Express	Priority Basic	Xpresspost
INTL_SURFACE	N/A 	            N/A	1st Class International	N/A	N/A
INTL_PRIORITY 	International       Economy	Worldwide Saver	Priority International 	N/A	N/A
INTL_EXPRESS	International       Priority
'''


config_register(MultipleStringValue(
    SATCHMO_SHIP_GROUP,
    'FEDEX_SERVICES',
    description=_("Fedex Services"),
    help_text=_("Which Fedex services are available to ship with?"),
    choices=[
        ('fedex_ground', _('Ground/Home')),
        ('fedex_exp_saver', _('Express Saver')),
        ('fedex_2day', _('2Day')),
        ('fedex_2day_am', _('2Day AM')),
        ('fedex_std_ovnt', _('Standard Overnight')),
        ('fedex_prty_ovnt', _('Priority Overnight')),
        ('fedex_firsusps_t_ovnt', _('First Overnight')),
        ('fedex_intl_eco', _('International Economy')),
        ('fedex_intl_prty', _('International Priority')),
        ]))
config_register(MultipleStringValue(
    SATCHMO_SHIP_GROUP,
    'UPS_SERVICES',
    description=_("UPS Services"),
    help_text=_("Which UPS services are available to ship with?"),
    choices=[
        ('ups_ground', _('Ground')),
        ('ups_3day', _('3 Day Select')),
        ('ups_2day', _('2nd Day Air')),
        ('ups_2day_am', _('2nd Day Air AM')),
        ('ups_nday_air_sav', _('Next Day Air Saver')),
        ('ups_nday', _('Next Day Air')),
        ('ups_nday_early', _('Next Day Air Early AM')),
        ('ups_world_sav', _('Worldwide Saver')),
        ('ups_world_exp', _('Worldwide Express')),
        ]))

config_register(MultipleStringValue(
    SATCHMO_SHIP_GROUP,
    'CARRIERS',
    description=_("Carriers"),
    help_text=_("Which USPS services are available to ship with"),
    choices=[
        ('usps', _('USPS')),
        ('fedex', _('Fedex')), #3day
        ('UPS', _('UPS'))
    ],
))


