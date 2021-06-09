from django.db import models
from django.urls import reverse
from django.core.management import call_command

class AmountInfo(models.Model):
    legal = models.PositiveIntegerField()
    gl_amount_balance = models.FloatField()


class FTPCredentials(models.Model):
    ftp_url= models.CharField(max_length=80, help_text='FTP URL to login', default='ftp.quantfarm.com')
    ftp_username= models.CharField(max_length=40, help_text='Username', default='eash.iyer@quantfarm.com')
    ftp_password= models.CharField(max_length=40, help_text='Password', default='F!leZ!ll@')
    ftp_filename= models.CharField(max_length=40, help_text='Name of file, which need to be loaded', default='Temp_File.csv')

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    execution_time_sec = models.PositiveSmallIntegerField(default=0)

    EXECUTION_STATUSES = (
        ('Not Started', 'Not Started'),
        ('Running', 'Running'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    )
    status = models.CharField(choices=EXECUTION_STATUSES, default='Not Started', max_length=11)

    def get_absolute_url(self):
        call_command('load_data'), 
        #     ftp_url ='ftp.quantfarm.com', 
        #     ftp_username ='eash.iyer@quantfarm.com',
        #     ftp_password = 'F!leZ!ll@', 
        #     ftp_filename = 'Temp_File.csv'
        # )
        return reverse('detail_view', args=[str(self.id)])
