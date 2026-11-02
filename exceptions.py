class MaintenanceRequiredError(Exception):
    """Wird ausgelöst, wenn ein Fahrzeug gewartet werden muss."""
    pass


class InvalidMileageError(ValueError):
    """Wird ausgelöst bei ungültigem Kilometerstand."""
    pass