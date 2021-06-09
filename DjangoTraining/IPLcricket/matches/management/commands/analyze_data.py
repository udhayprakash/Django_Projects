#!/usr/bin/python
"""
Purpose:
"""
from django.core.management.base import BaseCommand
from matches.models import MatchesPlayed, Deliveries
from django.db.models import Count, Q, Sum


def main():
    for each in MatchesPlayed.objects.values():
        print(each)


class Command(BaseCommand):
    help = 'Analyze data'

    def handle(self, *args, **kwargs):
        main()
