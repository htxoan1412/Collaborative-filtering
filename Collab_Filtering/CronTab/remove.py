from crontab import CronTab

my_cron = CronTab(user=True)
for job in my_cron:
    # print(job)
    # if job.comment == 'dateinfo':
    my_cron.remove_all()
    my_cron.write()