# import csv data and match to model
import csv
from library.models import MusicItem

def csvToDb(filename):

     with open(filename) as f:
        reader = csv.reader(f)

        for row in reader:
            obj, created = MusicItem.objects.get_or_create(
                inventory_num = row[0],
                title = row[1],
                composer_last = row[2],
                composer_first = row[3],
                arranger_last = row[4],
                arranger_first = row[5],
                ensemble = row[6],
                style = row[7],
                difficulty = row[8],
                rating = row[9],
                last_performed = row[10],
                organized = False,
                notes = row[12],
                )

csvToDb("test_data.csv")
