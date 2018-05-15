
from myapp import app

from flask import render_template, request, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import required
from myapp.models.Locality import Locality

import logging
import json

import urllib
import urllib2

import socket


class MyForm(FlaskForm):
    site_url = StringField('site URL', [required()])
    submit = SubmitField('submit', [required()])


@app.route('/check', methods=['GET'])
def showForm():
    form=MyForm()
    return render_template('check.html', form=form)


@app.route('/check', methods=['POST'])
def submitForm():
    form = MyForm(request.form)
    if not form.validate():
        return render_template('check.html', form=form), 400

    url_inserted = form.site_url.data

    url = 'https://validator.w3.org/nu/'

    param = {
        'doc': url_inserted,
        'out': 'json'
    }

    params = urllib.urlencode(param)

    myurl = '{}?{}'.format(url, params)

    logging.info('myurl: {}'.format(myurl))

    req = urllib2.Request(myurl)
    urlresp = urllib2.urlopen(req)
    content = urlresp.read()
    risp = json.loads(content)

    # retrieve locality

    # pay attention: remove the Hypertext Transfer Protocol to use socket method correctly
    if url_inserted.startswith('https://'):
        host = url_inserted[8:]

    elif url_inserted.startswith('http://'):
        host = url_inserted[7:]

    ip_address = socket.gethostbyname(host)

    url2 = 'https://api.ip2country.info/ip'

    myurl2 = '{}?{}'.format(url2, ip_address)

    logging.info('myurl: {}'.format(myurl2))

    req2 = urllib2.Request(myurl2)
    urlresp2 = urllib2.urlopen(req2)
    content2 = urlresp2.read()
    risp2 = json.loads(content2)

    loc = risp2['countryName']

    # save in Datastore
    qry = Locality.query(Locality.name == loc).get()

    if not qry:
        new_loc = Locality(name=loc, counter=1)
        new_loc.put()
        logging.info('Correctly inserted {}'.format(loc))

    else:
        qry.counter = qry.counter+1
        qry.put()
        logging.info('Correctly updated {}'.format(loc))

    return render_template('response.html', risp=risp, loc=loc)