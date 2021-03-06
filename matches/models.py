from django.db import models
from teams.models import Team

class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team_1")
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team_2")
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=120)
    score = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return self.first_team.name + '\t vs \t' + self.second_team.name