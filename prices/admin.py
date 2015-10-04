from django.contrib import admin

from prices.models import Category, Tag, Unit, Lang, Good
# Register your models here.
admin.site.register( Category )
admin.site.register( Tag )
admin.site.register( Unit )
admin.site.register( Lang )
admin.site.register( Good )
