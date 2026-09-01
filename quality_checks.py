def check_moisture(moisture_level):
    if moisture_level > 8:
        return "WARNING: Moisture too high! Beans might rot."
    else:
        return "Moisture level is safe."