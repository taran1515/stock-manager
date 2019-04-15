from django.contrib import admin
from .models import Purchase, Stock, Sale


class CompanyFilter(admin.SimpleListFilter):
    title = ('Company')
    parameter_name ='company'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.company,id.company))
        print (tuple(lst))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(company__exact=self.value())


class ModelFilter(admin.SimpleListFilter):
    title = ('Model')
    parameter_name ='model_no'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.model_no,id.model_no))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(model_no__exact=self.value())


class ColourFilter(admin.SimpleListFilter):
    title = ('Colour')
    parameter_name ='color'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.color,id.color))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(color__exact=self.value())


class SupplierFilter(admin.SimpleListFilter):
    title = ('Supplier')
    parameter_name ='supplier'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.supplier,id.supplier))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(supplier__exact=self.value())

class DateFilter(admin.SimpleListFilter):
    title = ('Date of Purchase')
    parameter_name ='date_of_purchase'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    contlist = list(Purchase.objects.all())

    def lookups(self, request, model_admin):
        lst = []
        for id in self.contlist:
            lst.append((id.date_of_purchase,id.date_of_purchase))
        return tuple(lst)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(date_of_purchase__exact=self.value())