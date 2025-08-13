
from django.core.management.base import BaseCommand
from trains.models import Station, Train, Stop
import random
from datetime import time

class Command(BaseCommand):
    help = "Generate test data for trains"

    def handle(self, *args, **kwargs):
        Stop.objects.all().delete()
        Train.objects.all().delete()
        Station.objects.all().delete()

        # Create 30 stations
        stations = [Station.objects.create(name=f"Station {i}") for i in range(1, 31)]

        # Create 1000 trains
        for i in range(1, 101):
            train = Train.objects.create(name=f"Train {i}")
            num_stops = random.randint(5, 15)
            route_stations = random.sample(stations, num_stops)

            current_hour = random.randint(0, 20)
            current_minute = random.choice([0, 15, 30, 45])

            for order, station in enumerate(route_stations):
                if order == 0:
                    distance = 0
                else:
                    distance = random.randint(50, 300)
                departure_time = time((current_hour + order) % 24, current_minute)
                Stop.objects.create(
                    train=train,
                    station=station,
                    distance_from_previous=distance,
                    departure_time=departure_time,
                    order=order
                )

        self.stdout.write(self.style.SUCCESS("Generated 1000 trains successfully."))
