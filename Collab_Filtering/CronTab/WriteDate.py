import datetime

with open('F:\DATN\shoesecommerce\Collab_Filtering\ShopSystem\dateInfo.txt', 'a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))