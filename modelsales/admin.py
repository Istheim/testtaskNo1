from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import NetworkElement


class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_level_display', 'supplier', 'debt', 'city', 'user')
    list_filter = ('level', 'supplier', 'city', 'user')  # Добавлены фильтры

    def supplier_link(self, obj):
        supplier_name = dict(NetworkElement.LEVELS_CHOICES).get(obj.supplier, obj.supplier)
        url = reverse('admin:yourappname_networkelement_change', args=[obj.supplier])
        return format_html('<a href="{}">{}</a>', url, supplier_name)

    supplier_link.short_description = 'Supplier'

    def clean_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, f'Debt cleared for selected network elements.')

    clean_debt.short_description = "Clear Debt for Selected Network Elements"


admin.site.register(NetworkElement, NetworkElementAdmin)
