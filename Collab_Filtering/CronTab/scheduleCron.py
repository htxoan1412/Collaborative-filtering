from crontab import CronTab

my_cron = CronTab(user=True)
job = my_cron.new(command='python F:/DATN/shoesecommerce/Collab_Filtering/CronTab/WriteDate.py', comment='resetDB')
job.minute.every(1)
my_cron.write()
# F:\DATN\shoesecommerce\Collab_Filtering\CronTab\scheduleCron.py

