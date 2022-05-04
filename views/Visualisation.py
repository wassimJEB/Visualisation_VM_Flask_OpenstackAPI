import urllib.request , urllib.parse
from urllib.error import HTTPError, URLError
import json
from flask import Flask ,jsonify
from connect import *

######################################"Other Function##########################
def listOfServer(mytoken):

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    # Build the URL
    CMDpath = "/v2.1/servers/detail"
    APIport = NOVAport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)

    for i in (decoded1['servers']):
    	print(i['name'])
    	print(i['status'])
    	print(i['flavor']['id'])
    	print(i['image']['id'])
		# for address in i['addresses']['provider']:
			# print address['addr']

    return decoded1;


def listOfFlavors(mytoken):
    # mytoken = getAdminToken()

    print("*  Get list of the Images details  *")

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    # Build the URL
    CMDpath = "/v2.1/flavors/detail"
    APIport = NOVAport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    print(req1)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    for i in decoded1['flavors']:
        print(i['name'], i['id'])

    return decoded1;


def listOfImages(mytoken):

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    # Build the URL
    # http://localhost:9292/v2/images
    CMDpath = "/v2/images"
    APIport = GLANCEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)
    for i in decoded1['images']:
        print(i['name'], i['id'])
    return decoded1;


def listOfNetworks(mytoken):

    # Build the headers

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': mytoken
    }
    print("REQUEST HEADERS", headers)

    # Build the URL
    # http://localhost:9696/v2.0/networks
    CMDpath = "/v2.0/networks"
    APIport = NEUTRONport
    url1 = "http://" + hostIP + ":" + APIport + CMDpath
    print("URL", url1)
    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)
    for i in decoded1['networks']:
        print(i['name'], i['id'])
    return decoded1;


def listOfProjects(mytoken):
    # mytoken = getAdminToken()

    print("*  Get list of the Images details  *")

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    # Build the request URL
    CMDpath = "/v3/projects"
    APIport = KEYSTONEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    for i in decoded1['projects']:
        print(i['name'], i['id'])
    return decoded1;
def listOfUsers(mytoken):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)
    # Build the request URL
    CMDpath = "/v3/users"
    APIport = KEYSTONEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    for i in decoded1['users']:
        print(i['name'], i['id'])
    return decoded1;


##################Flavor actions #############################""
def getFlavorNameById(mytoken, flavorId):
    print("Build the request headers, URL and body and GET everything")

    # Build the headers

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': mytoken
    }
    print("REQUEST HEADERS", headers)

    # Build the URL
    CMDpath = "/v2.1/flavors/" + flavorId
    APIport = NOVAport
    url1 = "http://" + hostIP + ":" + APIport + CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    print(req1)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    flavorName = decoded1['flavor']['name']
    print(flavorName)
    return flavorName;

######################################################################""
##################image actions #############################""

def getImageNameById(mytoken, imageId):
    print("Build the request headers, URL and body and GET everything")

    # Build the headers

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': mytoken
    }
    print("REQUEST HEADERS", headers)

    # Build the URL
    CMDpath = "/v2.1/images/" + imageId
    APIport = NOVAport
    url1 = "http://" + hostIP + ":" + APIport + CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    print(req1)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    imageName = decoded1['image']['name']
    print(imageName)
    return imageName;

######################################################################""
##################Server actions #############################""


def getServerUsage(mytoken, projectId):
    # mytoken = getAdminToken()
    # Build the headers

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': mytoken
    }
    print("REQUEST HEADERS", headers)

    # Build the URL
    # http://localhost:8774/v2.1/os-simple-tenant-usage/65a1fb5b49aa49a8a82ee57db2ca38fa
    CMDpath = "/v2.1/os-simple-tenant-usage/" + projectId
    APIport = NOVAport
    url1 = "http://" + hostIP + ":" + APIport + CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)
    print(req1)
    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    # print "RESPONSE (FORMATTED)" ; print "====================" ; print pretty1 ; print "" ; print ""

    return decoded1;


######################################################################""