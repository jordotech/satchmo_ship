from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from satchmo_store.shop.models import Order, OrderItem
import datetime
from django.db.models.signals import pre_delete
import logging
logger = logging.getLogger('tasks')
class OrderPackageItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"))
    order_item = models.ForeignKey(OrderItem, verbose_name=_("Order Item"), blank=True,)
    quantity = models.DecimalField(_("Quantity"),  max_digits=18,  decimal_places=6)
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = _('Order Package Item')
        verbose_name_plural = _('Order Package Items')
    def __unicode__(self):
        return 'Order %s %sX %s' % (self.order_id, round(self.quantity), self.order_item)


class OrderPackage(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"))

    @property
    def weight(self):
        total = 0
        for i in self.order_package_items.all():
            total += i.order_item.product.weight
        return total
    cost = models.DecimalField(_("Cost"), max_digits=6, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    ship_date = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    width = models.DecimalField(_("Width"), max_digits=6, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(_("Length"), max_digits=6, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(_("Height"), max_digits=6, decimal_places=2, null=True, blank=True)
    weight_units = models.CharField(_("Weight units"), max_length=3, null=True, blank=True)
    dimension_units = models.CharField(_("Dimension units"), max_length=3, null=True, blank=True)
    tracking = models.CharField(_("Tracking"), max_length=255, blank=True,)
    carrier = models.CharField(_("Carrier"), max_length=255, blank=True,)
    notes = models.TextField('Notes', blank=True,null=True)
    label = models.TextField('Label', blank=True,null=True)
    order_package_items = models.ManyToManyField(OrderPackageItem, blank=True,)

'''
class OrderShipment(models.Model):
    order_packages = models.ManyToManyField(OrderPackage, blank=True,)
'''

def delete_order_package_items(sender, instance, using, **kwargs):
    logger.debug(instance)

    instance.order_package_items.all().delete()
pre_delete.connect(delete_order_package_items, sender=OrderPackage)