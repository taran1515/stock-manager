from django.contrib import admin
from .models import Purchase, Stock, Sale
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from .purchase_filter import CompanyFilter, ModelFilter, ColourFilter, SupplierFilter, DateFilter


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('company','model_no','color','price','quantity','supplier','date_of_purchase')
    list_filter = [CompanyFilter, ModelFilter, ColourFilter, SupplierFilter, DateFilter]
    search_fields = ('company', 'model_no')
    date_


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('company', 'model_no', 'color', 'quantity')
    list_display_link=None
    readonly_field = ('company',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('company','model_no','color','price','quantity','retailer','date_of_sale')


