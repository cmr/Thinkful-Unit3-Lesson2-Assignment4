import csv
import psycopg2

#----------------------------------------------------------
# Parse CSV entries.

reader = csv.DictReader(open('pets_to_add.csv'))

result = {}
for row in reader:
    for column, value in row.iteritems():
        result.setdefault(column, []).append(value)
#        return result

#-----------------------------------------------------------
# Psycopg2 module methods to add CSV entries to DB.

try:
    conn=psycopg2.connect("dbname='petsdb'")
except:
    print "I am unable to connect to the database."
    
cur = conn.cursor()

cur.execute("INSERT INTO pets (name, age, breed name, species name, shelter name, adopted) VALUES (%s, %s, %s, %s, %s, %s)", (result))

# Make the changes to the database persistent
#conn.commit()

# Close communication with the database
#cur.close()
#conn.close()
            
#-----------------------------------------------------------
# Script's main function.

#if __name__ == "__main__":
#    csv_path = "pets_to_add.csv"
#    with open(csv_path, "rb") as f_obj:
#        csv_reader(f_obj)