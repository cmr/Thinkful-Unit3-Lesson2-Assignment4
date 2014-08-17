import csv, sys
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
# Test psycopg2

#con = None

#try:
    
#    con = psycopg2.connect(database='pets')
#    cur = con.cursor()
#   cur.execute('SELECT version()')
#    ver = cur.fetchone()
#    print ver
    
#except psycopg2.DatabaseError, e:
#    print 'Error %s' % e
#    sys.exit(1)
    
#finally:
    
#    if con:
#        con.close()
        
#-----------------------------------------------------------
# Psycopg2 module methods to add CSV entries to DB.

try:
    con = psycopg2.connect("dbname='petsdb'")
    
    cur = con.cursor()

    cur.execute("INSERT INTO pets (name, age, breed name, species name, shelter name, adopted) VALUES (%s, %s, %s, %s, %s, %s)", (result))

    # Make the changes to the database persistent
    con.commit()
    
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
        
    print 'Error %s' % e
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
    
# Close communication with the database
#cur.close()
#conn.close()
            
#-----------------------------------------------------------
# Script's main function.

#if __name__ == "__main__":
#    csv_path = "pets_to_add.csv"
#    with open(csv_path, "rb") as f_obj:
#        csv_reader(f_obj)