import sql
from pgsql import query
import csv


#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert2, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert3, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert4, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert5, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert6, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert7, row)

#with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv', newline='',
    #encoding="utf-8-sig") as f:
    #reader = csv.reader(f, delimiter=',')
    #next(reader)
    #for row in reader:
        #row.pop()
        #print(row)
        #query(sql.create_insert8, row)

with open ('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv', newline='',
    encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        #row.pop()
        #print(row)
        query(sql.create_insert9, row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
    #query(sql.test_insert, ["My Insert!"]);

    # select data
    #results = query(sql.test_select);
    #print("results: ", results)

    # create schema
    #query(sql.create_schema);

    # create tables
    #query(sql.create_table);
    #query(sql.create_table2);
    #query(sql.create_table3);
    #query(sql.create_table4);
    #query(sql.create_table5);
    #query(sql.create_table6);
    #query(sql.create_table7);
    #query(sql.create_table8);
    #query(sql.create_table9);

    # insert data
    #query(sql.create_insert);
    #query(sql.create_insert2);
    #query(sql.create_insert3);
    #query(sql.create_insert4);
    #query(sql.create_insert5);
    #query(sql.create_insert6);
    #query(sql.create_insert7);
    #query(sql.create_insert8);
    query(sql.create_insert9);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
