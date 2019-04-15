from django.contrib import admin
from .models import Purchase, Stock, Sale

class PurchaseFilter(admin.SimpleListFilter):
    title = ('Company')

    parameter_name ='company'

    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.company,id.company))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(company__exact=self.value())
