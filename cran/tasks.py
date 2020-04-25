from .celery import app
from .models import Package
import logging
import time
from .utilites import get_description_from_url, parse_description, parse_package, get_updated_packages

logger = logging.getLogger(__name__)
base_url = "http://cran.r-project.org/src/contrib/"

@app.task
def update_packages():
    # check if refresh is required
    packages = get_updated_packages()
    if packages == None:
        logging.info("Package ETag is not changed, nothing to update...")
        return False
    logging.info("Downloaded package list, total items = " + str(len(packages)))
    for package in packages:
        update_package_info.delay(package)

@app.task
def update_package_info(package):
    # Parse Package Information
    result = parse_package(package)
    if result == None:
        return False

    # build package url from name & version 
    url = base_url + result["name"] + "_" + result["version"] + ".tar.gz"
    logging.info("started processing url : " + url)

    # Skip if package informtion is already processed.
    if Package.objects.filter(name=result["name"], version=result["version"]).exists() :
        logging.info("Package ({}) version ({}) metadata already in database".format(result["name"], result["version"]))
        return True

    # get description from url
    description = get_description_from_url(url, result["name"])

    # Parse DESCRIPTION
    description = parse_description(description)

    # Store Package information in Database
    p = Package()
    p.from_dict(description)
    p.save()

    logging.info("done, object count = " + str(Package.objects.all().count()))