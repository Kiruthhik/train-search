
# from django.shortcuts import render
# from .models import Station, Train, Stop
# from datetime import datetime

# PRICE_PER_KM = 1.25

# def search_view(request):
#     stations = Station.objects.all()
#     return render(request, "trains/search.html", {"stations": stations})

# def results_view(request):
#     source_id = request.GET.get("source")
#     destination_id = request.GET.get("destination")
#     sort_by = request.GET.get("sort", "price")

#     if not (source_id and destination_id):
#         return render(request, "trains/results.html", {"error": "Please select both stations."})

#     source = Station.objects.get(id=source_id)
#     destination = Station.objects.get(id=destination_id)

#     trains_data = []

#     for train in Train.objects.all():
#         stops = train.stops.all().order_by("order")
#         source_stop = next((s for s in stops if s.station == source), None)
#         dest_stop = next((s for s in stops if s.station == destination), None)

#         if source_stop and dest_stop and source_stop.order < dest_stop.order:
#             total_distance = sum(s.distance_from_previous for s in stops if source_stop.order < s.order <= dest_stop.order)
#             price = total_distance * PRICE_PER_KM
#             trains_data.append({
#                 "train": train.name,
#                 "departure": source_stop.departure_time,
#                 "arrival": dest_stop.departure_time,
#                 "distance": total_distance,
#                 "price": price
#             })

#     if sort_by == "price":
#         trains_data.sort(key=lambda x: x["price"])
#     elif sort_by == "time":
#         trains_data.sort(key=lambda x: x["departure"])

#     return render(request, "trains/results.html", {
#         "source": source,
#         "destination": destination,
#         "trains": trains_data
#     })


# trains/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Station, Train
from datetime import datetime

PRICE_PER_KM = 1.25

def home(request):
    stations = Station.objects.all().order_by('name')
    return render(request, "trains/home.html", {"stations": stations})

def search_trains(request):
    source_id = request.GET.get("source")
    destination_id = request.GET.get("destination")
    sort_by = request.GET.get("sort", "price")

    if not source_id or not destination_id:
        return JsonResponse({"html": "<p>Please select both source and destination.</p>"})

    source = Station.objects.get(id=source_id)
    destination = Station.objects.get(id=destination_id)

    trains_data = []
    for train in Train.objects.all():
        stops = train.stops.all().order_by("order")
        source_stop = next((s for s in stops if s.station == source), None)
        dest_stop = next((s for s in stops if s.station == destination), None)

        if source_stop and dest_stop and source_stop.order < dest_stop.order:
            total_distance = sum(
                s.distance_from_previous
                for s in stops
                if source_stop.order < s.order <= dest_stop.order
            )
            price = round(total_distance * PRICE_PER_KM, 2)
            trains_data.append({
                "train": train.name,
                "departure": source_stop.departure_time.strftime("%H:%M"),
                "arrival": dest_stop.departure_time.strftime("%H:%M"),
                "distance": total_distance,
                "price": price
            })

    if sort_by == "price":
        trains_data.sort(key=lambda x: x["price"])
    elif sort_by == "time":
        trains_data.sort(key=lambda x: x["departure"])

    html = render(request, "trains/results_partial.html", {
        "trains": trains_data,
        "source": source,
        "destination": destination
    }).content.decode("utf-8")

    return JsonResponse({"html": html})

