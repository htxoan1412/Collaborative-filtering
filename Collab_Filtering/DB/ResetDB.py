import pymysql as db
import csv

connection = db.connect(host='localhost', user='root', password='12345678', db='ecommerceShoes')
print("connect succssful!")

try:
    with connection.cursor() as cursor:

        sql = "SELECT * FROM suggest"
        result_count = cursor.execute(sql)
        rows = cursor.fetchall()
        # print(" sádsd",rows)
        # for j in rows:

        # column_names = [i[1] for i in cursor.description]
        c = csv.writer(open('F:/DATN/shoesecommerce/Collab_Filtering/ShopSystem/CF.csv', "w"), lineterminator='\n')
        c.writerows(rows)
finally:
    connection.close()
