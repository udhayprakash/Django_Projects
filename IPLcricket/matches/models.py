from django.db import models


# Create your models here.
class MatchesPlayed(models.Model):
    id = models.AutoField(primary_key=True)
    season = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    toss_winner = models.CharField(max_length=30)
    toss_decision = models.CharField(max_length=5)
    result = models.CharField(max_length=10)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length=30)
    win_by_runs = models.PositiveSmallIntegerField()
    win_by_wickets = models.PositiveSmallIntegerField()
    player_of_match = models.CharField(max_length=30, blank=True)
    venue = models.CharField(max_length=55)
    umpire1 = models.CharField(max_length=30, blank=True)
    umpire2 = models.CharField(max_length=30, blank=True)
    umpire3 = models.CharField(max_length=30, blank=True)

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"


class Deliveries(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.PositiveSmallIntegerField()
    inning = models.PositiveSmallIntegerField()
    batting_team = models.CharField(max_length=30)
    bowling_team = models.CharField(max_length=30)
    over = models.PositiveSmallIntegerField()
    ball = models.PositiveSmallIntegerField()
    batsman = models.CharField(max_length=30)
    non_striker = models.CharField(max_length=30)
    bowler = models.CharField(max_length=30)
    is_super_over = models.BooleanField()
    wide_runs = models.PositiveSmallIntegerField()
    bye_runs = models.PositiveSmallIntegerField()
    legbye_runs = models.PositiveSmallIntegerField()
    noball_runs = models.PositiveSmallIntegerField()
    penalty_runs = models.PositiveSmallIntegerField()
    batsman_runs = models.PositiveSmallIntegerField()
    extra_runs = models.PositiveSmallIntegerField()
    total_runs = models.PositiveSmallIntegerField()
    player_dismissed = models.CharField(max_length=30)
    dismissal_kind = models.CharField(max_length=30)
    fielder = models.CharField(max_length=30)

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"
