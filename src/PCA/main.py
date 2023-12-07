
# Imports the Google Cloud client library
from google.cloud import vision

def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ProductSearchClient()

    # The URI of the image file to annotate
    file_uri = "gs://cloud-samples-data/vision/label/wakeupcat.jpg"

    image = vision.Image()
    image.source.image_uri = file_uri

    # Performs label detection on the image file
    response = client.create_product_set(request=image)
    return response

def main():
    run_quickstart()

if __name__ == "__main__":
    main()