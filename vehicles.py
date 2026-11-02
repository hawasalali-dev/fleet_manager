from fleet.exceptions import (
    MaintenanceRequiredError,
    InvalidMileageError
)


class Vehicle:
    SERVICE_INTERVAL = 15000

    def __init__(self, license_plate, mileage, last_service_km):
        if mileage < 0:
            raise InvalidMileageError(
                "Kilometerstand darf nicht negativ sein."
            )

        self.license_plate = license_plate
        self.mileage = mileage
        self.last_service_km = last_service_km

    def needs_service(self):
        return (self.mileage - self.last_service_km) > self.SERVICE_INTERVAL

    def calculate_trip_cost(self, distance):
        raise NotImplementedError(
            "Methode muss überschrieben werden."
        )

    def drive(self, distance):
        self.mileage += distance

        if self.needs_service():
            raise MaintenanceRequiredError(
                f"{self.license_plate} benötigt Wartung!"
            )

    def __str__(self):
        return (
            f"{self.license_plate} "
            f"({self.mileage} km)"
        )


class FuelVehicle(Vehicle):

    def __init__(
        self,
        license_plate,
        mileage,
        last_service_km,
        fuel_consumption_per_100km,
        fuel_price_per_liter
    ):
        super().__init__(
            license_plate,
            mileage,
            last_service_km
        )

        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price_per_liter = fuel_price_per_liter

    def calculate_trip_cost(self, distance):
        fuel_used = (
            distance / 100
        ) * self.fuel_consumption_per_100km

        return fuel_used * self.fuel_price_per_liter


class EVehicle(Vehicle):

    def __init__(
        self,
        license_plate,
        mileage,
        last_service_km,
        kwh_per_100km,
        electricity_price_per_kwh
    ):
        super().__init__(
            license_plate,
            mileage,
            last_service_km
        )

        self.kwh_per_100km = kwh_per_100km
        self.electricity_price_per_kwh = (
            electricity_price_per_kwh
        )

    def calculate_trip_cost(self, distance):
        energy_used = (
            distance / 100
        ) * self.kwh_per_100km

        return (
            energy_used
            * self.electricity_price_per_kwh
        )