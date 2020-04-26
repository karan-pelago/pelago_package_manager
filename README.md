### Background / What is CRAN?
CRAN is a network of ftp and web servers around the world that store identical, up-to-date,
versions of code and documentation for R. The R project uses these CRAN Servers to store R
packages.

A CRAN server looks like: http://cran.r-project.org/src/contrib/. It is just a simple Apache Dir with
a bunch of tar.gz files.

### PACKAGES file

Every CRAN server contains a plain file listing all the packages in that server. You can access it
using this URL: http://cran.r-project.org/src/contrib/PACKAGES

### Format of PACKAGES file
[...]
Package: adehabitatHR
Version: 0.4.2
Depends: R (>= 2.10.0), sp, methods, deldir, ade4, adehabitatMA, adehabitatLT
Suggests: maptools, tkrplot, MASS, rgeos, gpclib
License: GPL (>= 2)
[...]

## What do we want to do?

We want you to create a application to index all the packages in a CRAN server with the
following requirements:

- [x] Extract some information regarding every package and store it (you will need to get
some info from the PACKAGES file and some other info from DESCRIPTION)
- [x] Create an API endpoint for search (something like /search?q=xyz) packages based
package name which returns the list of all the packages you have searched
- [x] Implement the business logic needed for storing all the information (models, libs, DB
structure...)
- [x] Push the code to a publicly-available git repository (e.g. GitHub, Bitbucket) and send us the URL


### What information do we want to store about a package?
- Package name
- Version
- Date/Publication
- Title
- Description
- Authors
- Maintainers And authors/maintainers?
- Name
- Email

-----------------

### Requirement
```
Pyhton 3.7+, Docker, Docker-compose
```

## TOOLS

##### Backend Development:
Django RESTful

##### Deployment
Docker | GCP | CloudFlare(DNS)

##### Database Development:
Postgres | SQLite


## Installation Guide
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

`$ pip install virtualenv`
`$ virtualenv .venv && source .venv/bin/activate`

If you wish to run your own build, you two options
 1. Use Docker.
    
    `$ git clone https://github.com/karanftd/pelago_package_manager.git`
    `$ cd pelago_package_manager`
    `$ docker-compose build`
    `$ docker-compose up`

 2. Without docker.
    `$ git clone https://github.com/karanftd/pelago_package_manager.git`
    `$ cd pelago_package_manager`
    Install dependancies
    `$ pip install -r requirements.txt`
    Make migrations & migrate
    `$ python manage.py makemigrations && python manage.py migrate`
    Launching the app
    `$ python manage.py runserver`


#### Endpoints
Method | Endpoint | Functionality
--- | --- | ---
GET | `/package` | List cran packages
GET | `/package?search=<package_name>` | Search package by package name

### example
#### List cran packages
```
curl --location --request GET 'http://127.0.0.1:8000/package' \
--header 'Content-Type: application/json'
```

#### Search package by name
```
curl --location --request GET 'http://127.0.0.1:8000/package?search=relevent' \
--header 'Content-Type: application/json'
```

### Hosted solution
I have hosted solution on Google Cloud VM

List cran packages
```
curl --location --request GET 'http://pelago.karanftd.com/package' \
--header 'Content-Type: application/json'
```

Search package by package name
```
curl --location --request GET 'http://pelago.karanftd.com/package?search=relevent' \
--header 'Content-Type: application/json'
```


<br/>
Thank you,
<br/>
Karan Bhalodiya