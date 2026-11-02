from fleet import (
    FuelVehicle,
    EVehicle,
    FleetAnalytics,
    MaintenanceRequiredError
)

fleet = [

    FuelVehicle(
        "K-AA-101",
        62000,
        43000,
        7.2,
        1.80
    ),

    FuelVehicle(
        "K-BB-202",
        48000,
        40000,
        5.9,
        1.75
    ),

    EVehicle(
        "K-CC-303",
        70000,
        52000,
        19,
        0.35
    ),

    EVehicle(
        "K-DD-404",
        35000,
        25000,
        16,
        0.32
    )
]

analytics = FleetAnalytics(fleet)

print("=== Fahrzeuge mit Servicebedarf ===")

service_vehicles = analytics.filter_vehicles(
    lambda v: v.needs_service()
)

for vehicle in service_vehicles:
    print(vehicle)

print("\n=== Fahrzeuge über 50.000 km ===")

high_mileage = analytics.filter_vehicles(
    lambda v: v.mileage > 50000
)

for vehicle in high_mileage:
    print(vehicle)

print("\n=== Fahrtkosten für 250 km ===")

for vehicle in fleet:
    cost = vehicle.calculate_trip_cost(250)

    print(
        f"{vehicle.license_plate}: "
        f"{cost:.2f} €"
    )

cheapest_vehicle = min(
    fleet,
    key=lambda v: v.calculate_trip_cost(250)
)

print(
    f"\nGünstigstes Fahrzeug: "
    f"{cheapest_vehicle.license_plate}"
)

print("\n=== Test Wartung ===")

try:
    fleet[1].drive(10000)

except MaintenanceRequiredError as error:
    print("WARNUNG:", error)