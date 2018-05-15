# Project Title

HTML quality code tester

## The project in short

Simple Google App Engine Web Application example with minimal style, written in Python 2.7, using W3C-Markup Validation Service site API 
(see references in "Built With" section).
The app is able to test the HTML quality code of a site, given by its complete URL, and to retrieve the locality of the 
server, which hosts the site.

## Specifications

- A form is used to retrieve the site URL, inserted by user.
- The app response shows: site URL, validation messages (or a subset of the available ones), server locality.
- Server locality and a counter are saved automatically in the Datastore.
- An API GET is given; it shows the 3 most requested servers locality, in JSON format.

## Before starting
Add a lib folder to the project, in which you have to install the libraries listed in "requirements.txt" file.

## Built With

* [Google App Engine](https://cloud.google.com/appengine/doc) - Platform used
* [Flask](http://flask.pocoo.org/) - The microframework for Python used
* [W3C-Markup Validation Service](https://validator.w3.org/) - API used
* [IP Geolocation](https://ip2country.info/) - API used

## Author

* **Marcella Tincani** - [Marcella](https://github.com/tmarcy)
