import requests
import time

from google.transit import gtfs_realtime_pb2 as gtfs
FEED_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm"


def create_feed(url):
    request = requests.get(url)
    request.raise_for_status()
    feed = gtfs.FeedMessage()
    feed.ParseFromString(request.content)
    return feed
#forest ave = M05N (northbound)
#forest ave = M05S (southbound)

def arrivals_for_stop(stop_id, limit_per_dir=2):
    now = int(time.time())
    feed = create_feed(FEED_URL)
    data = []
    for e in feed.entity:
        for nextArrival in e.trip_update.stop_time_update:
            if nextArrival.stop_id in stop_id:
                arrivalTime = nextArrival.arrival.time
                data.append(max((arrivalTime - now)//60,0))

    data.sort()
    return data


