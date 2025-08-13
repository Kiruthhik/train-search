# from django.core.management.base import BaseCommand
# from trains.models import Station, Train, Stop
# import random
# from datetime import time

# class Command(BaseCommand):
#     help = "Generate small test data for trains"

#     def handle(self, *args, **kwargs):
#         # Clear existing data
#         Stop.objects.all().delete()
#         Train.objects.all().delete()
#         Station.objects.all().delete()

#         # Create a few stations for testing
#         stations = [
#             Station.objects.create(name="Chennai"),
#             Station.objects.create(name="Vellore"),
#             Station.objects.create(name="Bangalore"),
#             Station.objects.create(name="Mysuru"),
#             Station.objects.create(name="Mangalore"),
#             Station.objects.create(name="Shimoga"),
#         ]

#         # Generate a small number of trains
#         for i in range(1, 6):  # 5 trains
#             train = Train.objects.create(name=f"Train {i}")
#             num_stops = random.randint(3, len(stations))  # between 3 and total stations
#             route_stations = random.sample(stations, num_stops)

#             current_hour = random.randint(5, 20)
#             current_minute = random.choice([0, 15, 30, 45])

#             for order, station in enumerate(route_stations):
#                 if order == 0:
#                     distance = 0
#                 else:
#                     distance = random.randint(50, 300)
#                 departure_time = time((current_hour + order) % 24, current_minute)
#                 Stop.objects.create(
#                     train=train,
#                     station=station,
#                     distance_from_previous=distance,
#                     departure_time=departure_time,
#                     order=order
#                 )

#         self.stdout.write(self.style.SUCCESS("Generated 5 trains successfully."))


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
            print(i)
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
