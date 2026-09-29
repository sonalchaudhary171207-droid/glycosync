from django.contrib import admin
from .models import GlucoseReading, SafetyRule


@admin.register(GlucoseReading)
class GlucoseReadingAdmin(admin.ModelAdmin):
    list_display = ('level_mgdl', 'meal_context', 'timestamp')
    list_filter = ('meal_context', 'timestamp')


@admin.register(SafetyRule)
class SafetyRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_name', 'is_safe')
    list_editable = ('is_safe',)