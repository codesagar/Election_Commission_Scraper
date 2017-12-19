import urllib.request
import urllib
import os, errno
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def election_result():
    to_visit = ["http://eciresults.nic.in/StatewiseS06.htm"]
    base = "http://eciresults.nic.in/StatewiseS06" + ".htm"
    x = "http://eciresults.nic.in/StatewiseS06"
    y = ".htm"
    next_pages = [x+str(n)+y for n in range(1,19)]
    to_visit.extend(next_pages)

    prefix = datetime.now().strftime('%Y-%m-%d_%H:%M')
    directory = "/home/sagar/eci_data/" + prefix + "/"

    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for idx, page in enumerate(to_visit):
        page_opener = urllib.request.URLopener()
        try:
            page_opener.retrieve(page, directory + "gujarat" + str(idx) + ".html")
        except:
            continue

    to_visit = ["http://eciresults.nic.in/StatewiseS08.htm"]
    base = "http://eciresults.nic.in/StatewiseS08" + ".htm"
    x = "http://eciresults.nic.in/StatewiseS08"
    y = ".htm"
    next_pages = [x+str(n)+y for n in range(1,6)]
    to_visit.extend(next_pages)

    for idx, page in enumerate(to_visit):
        page_opener = urllib.request.URLopener()
        try:
            page_opener.retrieve(page, directory + "himachal" + str(idx) + ".html")
        except:
            continue
    aggregate = "http://eciresults.nic.in/PartyWiseResult.htm"
    page_opener.retrieve(aggregate, directory + "aggregate.html")


scheduler = BlockingScheduler()
scheduler.add_job(election_result, 'interval', minutes=5)
scheduler.start()
