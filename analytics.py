class FleetAnalytics:

    def __init__(self, vehicles):
        self.vehicles = vehicles

    def filter_vehicles(self, predicate_fn):
        return list(
            filter(predicate_fn, self.vehicles)
        )

    def sort_vehicles(self, key_fn):
        return sorted(
            self.vehicles,
            key=key_fn
        )