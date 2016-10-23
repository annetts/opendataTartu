import csv
import json

csvfile = open('otsus.csv', 'r')
jsonfile = open('otsus.json', 'w')

fieldnames = ("Url","Id_custom","Tyyp_custom","Akti_valjaandja", "Akti_liik", "Teema", "Reg_nr", "Seisund","Vastuvotmise_kp", "Akti_kehtivus", "Url_SuurEelnou")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)

											
