def check_moisture(moisture_level):
    if moisture_level < 0:
        return "WARNING: Moisture too low! Beans might be too dry."
    if moisture_level <= 8:
        return "Moisture level is within the acceptable range."
    elif moisture_level <= 10:
        return "Fair. More drying might be needed."#
    else:
        return "WARNING: Moisture too high! Beans might be at risk of mold."

def get_quality_ratings(moisture_level):
    
    if moisture_level < 0:
        return "Invalid."
    if moisture_level <= 8:
        return "Good."
    elif moisture_level <= 10:
        return "Fair."
    else:
        return "Poor."