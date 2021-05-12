from bill.models import Order
import django_filters
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields=['bill_number','bill_date','customer_name']



# pip install django-filter
# install in settings
# filters py file
