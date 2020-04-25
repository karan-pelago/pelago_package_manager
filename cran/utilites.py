import re
import tarfile
import urllib.request
import io
from dateutil.parser import parse

# TODO: find a better way to persist this across restarts
last_check_etag = None

# TODO: move this to settings.py
package_url = "http://cran.r-project.org/src/contrib/PACKAGES"


def get_description_from_url(url, package):
    tar_file = urllib.request.urlopen(url)
    tar_handle = io.BytesIO(tar_file.read())
    f = tarfile.open(fileobj=tar_handle)
    description = f.extractfile(package +"/DESCRIPTION").read().decode("utf-8")
    return description
    
def parse_package(package):
    result = {}
    result["name"] = re.compile('Package:\s*.*').findall(package)[0].split(":")[1].strip()
    result["version"] = re.compile('Version:\s*.*').findall(package)[0].split(":")[1].strip() 
    return result

def parse_description(description):
    result = {}
    result["name"] = re.compile('Package:\s*.*').findall(description)[0].split(":")[1].strip()
    result["version"] = re.compile('Version:\s*.*').findall(description)[0].split(":")[1].strip()
    result["date"] = parse(re.compile('Date\S+:\s*.*').findall(description)[0].split(":",1)[1])
    result["title"] = re.compile('Title:\s*.*').findall(description)[0].split(":",1)[1].strip()
    result["author"] = re.compile('Author*:\s*.*').findall(description)[0].split(":",1)[1].strip()
    result["maintainer"] = re.compile('Version:\s*.*').findall(description)[0].split(":",1)[1].strip()
    result["description"] = re.compile('Description:\s*.*').findall(description)[0].split(":",1)[1].strip()
    depends = re.compile('Depends:\s*.*').findall(description)
    if (len(depends) == 0):
        depends = "N/A"
    else:
        depends = depends[0].split(":")[1].strip()
    result["depends"] = depends
    return result

def get_updated_packages():
    global last_check_etag
    response = urllib.request.urlopen(package_url)
    # let's save some bandwidth (and time), check ETag version!
    etag = response.info()["ETag"]
    if etag == last_check_etag :
        return None
    else:
        # download new packages list
        packages = response.read().decode('utf-8')
        last_check_etag = etag
        print ("storing etag : " + etag)
        return packages.split("\n\n")

    return None