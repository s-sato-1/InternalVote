from django.contrib import admin

# ====================================================

from .models import Award, AwardMst

# ====================================================

class AwardAdmin(admin.ModelAdmin):
    """ Award Loging
    """
    list_display = (
        'award_text',
	'employment_text',
	'prizewinner_text',
	'create_date',
    )
admin.site.register(Award, AwardAdmin)

class AwardMstAdmin(admin.ModelAdmin):
    """ Award Description
    """
    list_display = (
        'award_mst_text',
        'discription_text',
    )
admin.site.register(AwardMst, AwardMstAdmin)

