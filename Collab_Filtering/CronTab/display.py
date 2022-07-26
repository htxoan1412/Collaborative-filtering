from crontab import CronTab

cron = CronTab(user=True)

for item in cron:
    print(item)