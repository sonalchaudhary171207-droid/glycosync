from django.db import models


class GlucoseReading(models.Model):
    level_mgdl = models.IntegerField()
    meal_context = models.CharField(max_length=100, default='General')
    timestamp = models.DateTimeField(auto_auto_add=False, auto_now_add=True)

    def __str__(self):
        return f"{self.level_mgdl} mg/dL - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class SafetyRule(models.Model):
    rule_name = models.CharField(max_length=100)
    is_safe = models.BooleanField(default=True)

    def __str__(self):
        return self.rule_name