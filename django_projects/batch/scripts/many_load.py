import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco_more.models import Site, Category, Region, Iso, States


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    States.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            longi = int(row[4])
        except:
            longi = None

        try:
            lati = int(row[5])
        except:
            lati = None

        try:
            area = int(row[6])
        except:
            area = None

        site = Site(name=row[0], description=row[1], justification = row[2], year=y, longitude=longi, latitude = lati, area_hectares = area, category = c, states = s, region = r, iso = i)
        site.save()




        # site = Site.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Site(category=c, states=s, region=r, iso=i)
        # m.save()
