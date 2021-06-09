"""
Purpose: To connect to the ftp, 
    transform and dump to database
"""
import time
from ftplib import FTP
from ftp_to_db.models import AmountInfo, FTPCredentials
from django.core.management.base import BaseCommand

def dumplines_to_db(block, _records_to_db, file_handler):
    if block and row_data[-1].isnumeric():
        row_data = block.strip().split(',')
        if row_data[-1]:
            _records_to_db.append(
                AmountInfo(
                    legal = int(row_data[0]),
                    gl_amount_balance = 2 * float(row_data[-1])
                )
            )
        if len(_records_to_db) % 10000 == 0:
            AmountInfo.objects.bulk_create(_records_to_db)
            _records_to_db = []

def main(**ftp_creds):
    start_time = time.time()
    print(f'start time: {start_time}')
    latest_record = FTPCredentials.objects.latest('id')
    latest_record.status = 'Running'
    latest_record.save()
    # To delete existing data
    AmountInfo.objects.all().delete()
    print(f'Existing records count: {AmountInfo.objects.count()}')
    with FTP(latest_record.ftp_url) as ftp:
        ftp.login(latest_record.ftp_username, latest_record.ftp_password)
        ftp.cwd('/')

        filenames = ftp.nlst()
        for filename in filenames:
            if filename == latest_record.ftp_filename:
                records_to_db = []
                with open(filename, 'wb') as file :
                    ftp.retrlines('RETR %s' % filename, lambda blk: dumplines_to_db(blk, records_to_db, file))
                    file.close()
                print('Downloaded to local')
                if records_to_db:
                    AmountInfo.objects.bulk_create(records_to_db)
        ftp.quit()
    print(f'Existing records count: {AmountInfo.objects.count()}')
    end_time = time.time()
    print(f'end time  : {end_time}')
    print(f'TIME TAKEN: {(end_time - start_time)/60}')

    latest_record.status = 'Completed'
    latest_record.end_time = end_time
    latest_record.execution_time_sec = (end_time - start_time)
    latest_record.save()


class Command(BaseCommand):
    help='Command to laod data from ftp location to db'

    # def add_arguments(self, parser):
    #     parser.add_argument('ftp_url', type=str, help='ftp url')
    #     parser.add_argument('ftp_username', type=str, help='ftp username')
    #     parser.add_argument('ftp_password', type=str, help='ftp password')
    #     parser.add_argument('ftp_filename', type=str, help='ftp filename')

    def handle(self, *args, **kwargs):
        main(**kwargs)

# python manage.py load_data ftp_url ftp.quantfarm.com ftp_username eash.iyer@quantfarm.com ftp_password F!leZ!ll@ ftp_filename Temp_File.csv