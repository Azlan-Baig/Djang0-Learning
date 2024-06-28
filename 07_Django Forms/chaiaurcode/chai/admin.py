from django.contrib import admin
from .models import chaiVariery,Chai_review , store,ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
  model = Chai_review
  extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('chai_varieties', )

class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate_number')

admin.site.register(chaiVariery, ChaiVarityAdmin)
admin.site.register(store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
