import ee

def initialize_gee():
    try:
        ee.Initialize()
    except Exception:
        ee.Authenticate()
        ee.Initialize()

def load_image_collection(dataset, start_date, end_date):
    return ee.ImageCollection(dataset).filterDate(start_date, end_date)

# Add more GEE utility functions as needed
