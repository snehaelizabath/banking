from bank.bank import Bank
from django.contrib import admin

from homeapp.models import bank,registration

# Register your models here.
admin.site.register(bank)
admin.site.register(registration)