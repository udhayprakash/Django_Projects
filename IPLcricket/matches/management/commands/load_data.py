#!/usr/bin/python
"""
Purpose:
"""
from django.core.management.base import BaseCommand
import os
import csv
from IPLcricket import settings
from matches.models import MatchesPlayed, Deliveries
from datetime import datetime
from django.db.utils import DataError
import pandas as pd


def load_matches(file_name):
    file_path = os.path.join(settings.DOCS_PATH, file_name)

    with open(file_path, 'r') as fh:
        file_content = tuple(csv.DictReader(fh))
        print(f'total_records_count :{len(file_content):4}')

        newly_created_objs = 0
        for each_row in file_content:
            # print(each_row)
            if each_row['date']:
                each_row['date'] = datetime.strptime(each_row['date'], '%d-%m-%y')
            try:
                # # TO create a new object
                # obj = MatchesPlayed.objects.create(**each_row)
                # obj.save()
                _, is_new_obj = MatchesPlayed.objects.update_or_create(id=each_row.pop('id'), defaults=each_row)
                if is_new_obj:
                    newly_created_objs += 1
            except DataError as ex:
                print(ex)
        print(f'newly_created_objs  :{newly_created_objs:4}')


def load_deliveries(file_name):
    file_path = os.path.join(settings.DOCS_PATH, file_name)
    deliveries_df = pd.read_csv(file_path, delimiter=',', skip_blank_lines=True)
    print(f'total_records_count :{len(deliveries_df):4}')

    columns = tuple(deliveries_df.columns)
    newly_created_objs = 0
    for _index, each in deliveries_df.iterrows():
        each_obj = dict(each.items())
        # print(each_obj)
        try:
            _, is_new_obj = Deliveries.objects.update_or_create(id=_index+1, defaults=each_obj)
            if is_new_obj:
                newly_created_objs += 1
        except DataError as ex:
            print(ex)

    print(f'newly_created_objs  :{newly_created_objs:4}')


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='file to load')

    def handle(self, *args, **kwargs):
        file_name = kwargs.get('file_name')
        if file_name == 'matches.csv':
            load_matches(file_name)
        elif file_name == 'deliveries.csv':
            load_deliveries(file_name)
