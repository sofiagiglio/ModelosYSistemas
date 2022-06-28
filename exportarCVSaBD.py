import csv
import sqlite3

bd = sqlite3.connect("/home/alca/Escritorio/Ortiz_Balbuena_ProgII/JuegoClash/BDCLash.db")
c = bd.cursor()
sql ='INSERT INTO CARTAS (NOMBRE, DANIO, VIDA, URLFOTO) VALUES ("{}", {}, {}, "{}");'
with open('cardsInfo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            c.execute(sql.format(row[4], row[7], row[5], row[3]))
            print(row)
            line_count += 1
    print(f'Processed {line_count} lines.')
    bd.commit()