from .models import OrderPackage, OrderPackageItem

from django.contrib import admin
from django import forms
from satchmo_store.shop.models import OrderItem, Order


class OrderPackageModelForm(forms.ModelForm):
    class Meta:
        model = OrderPackage

    def __init__(self, *args, **kwargs):
        super(OrderPackageModelForm, self).__init__(*args, **kwargs)
        self.fields['order_package_items'] = forms.ModelMultipleChoiceField(required=False,
                                                                            queryset=OrderPackageItem.objects.filter(
                                                                                order=Order.objects.get(pk=9)))


class OrderPackageAdmin(admin.ModelAdmin):
    list_filter = ('order',)
    form = OrderPackageModelForm
    def item_count(self, obj):
        return obj.order_package_items.all().count()
    item_count.short_description = "Product Qty"
    list_display = ('id', 'created', 'ship_date', 'order', 'item_count', 'width', 'length', 'height', 'weight', 'tracking', 'label', 'cost')
    filter_horizontal = ('order_package_items',)


class OrderPackageItemModelForm(forms.ModelForm):
    class Meta:
        model = OrderPackageItem

    def __init__(self, *args, **kwargs):
        super(OrderPackageItemModelForm, self).__init__(*args, **kwargs)


class OrderPackageItemAdmin(admin.ModelAdmin):
    form = OrderPackageItemModelForm
    list_display = ('order_item', 'order', 'quantity')


admin.site.register(OrderPackage, OrderPackageAdmin)
admin.site.register(OrderPackageItem, OrderPackageItemAdmin)
