import os
os.system("sudo gpsd /dev/serial0 -F /var/run/gpsd.sock")
import gps
session = gps.gps("localhost","2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
cLon = 0
cLat = 0
pastLon = []
pastLat = []
while True:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report,'lon'):
                cLon = report.lon
                pastLon.append(cLon)
        if report['class'] == 'TPV':
            if hasattr(report,'lat'):
                cLat = report.lat
                pastLat.append(cLat)
        if len(pastLon) < 5:
            print(cLon,cLat)
        else:
            print(str(sum(pastLon[-5:])/5),end = ",")
            print(str(sum(pastLat[-5:])/5))
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")