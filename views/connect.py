import urllib.request , urllib.parse
from urllib.error import HTTPError, URLError
import json
from flask import Flask ,jsonify

############### you get this informmation via cloud.yaml ################
hostIP = "192.168.88.130"
domainName = "default"
user = "admin"
myPassword = "gkr1RDynOl6MCjpodlyKksFjSwL7Dlyl"
############### OpenStack API ports ########
NOVAport = "8774"
CINDERport = "8776"
CEILOMETERport = "8777"
GLANCEport = "9292"
NEUTRONport = "9696"
AWSport = "8000"
HEATport = "8004"
KEYSTONEport = "5000"
################Function to establish cnx##################
def getTokenDetail(userName, password, projectName):

    # Build the request headers
    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json'
               }
    print("REQUEST HEADERS:", headers)

    # Build the request URL
    CMDpath = "/v3/auth/tokens"
    APIport = KEYSTONEport
    url = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url)

    body = ('{'
    '   "auth": {'
    '       "identity": {'
    '           "methods": ['
    '               "password"'
    '           ],'
    '           "password": {'
    '               "user": {'
    '                   "domain": {'
    '                       "name": "default"'
    '                   },'
    '                   "name": "' + userName + '",'
    '                   "password": "' + myPassword + '"'
    '               }'
    '           }'
    '       },'
    '       "scope": {'
    '           "project": {'
    '               "domain": {'
    '                   "name": "default"'
    '               },'
    '               "name": "' + projectName + '"'
    '           }'
    '       }'
    '   }'
    '}')

    # Send the  POST request
    body = body.encode("utf-8")
    req = urllib.request.Request(url, body, headers)

    # Read the response header
    header = urllib.request.urlopen(req).info()
    print("RESPONSE HEADER===============", header)

    # Read the response body
    response = urllib.request.urlopen(req).read()
    print("RESPONSE BODY=============", response)

    # quit()

    print("Decode the response header and body")

    mytoken = header.get('X-Subject-Token')
    print("KEYSTONE TOKEN (X-Subject-Token) ================================", mytoken)
 # Convert response body to pretty print format
    decoded = json.loads(response.decode('utf8'))
    pretty = json.dumps(decoded, sort_keys=True, indent=3)
    print("RESPONSE BODY IN PRETTY FORMAT) ==============================", pretty)

    # Parse JSON formatted data for token issue date
    issued = (decoded['token']['issued_at']);

    # Parse JSON formatted data for token expiration date
    expires = decoded['token']['expires_at']
    print("TOKEN WILL EXPIRE=================", expires)
    projectId = decoded['token']['project']['id']
    domainId = decoded['token']['project']['domain']['id']
    tokenInfo = {'token': mytoken,
        'domainId': domainId, 'projectID': projectId}
    return tokenInfo;



def getToken(userName, password, projectName):

    print("* Obtain authorization token from Keystone *")

    print("Build the request headers, URL and body and POST everything     ")

    # Build the request headers
    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json'
               }
    print("REQUEST HEADERS:", headers)

    # Build the request URL
    CMDpath = "/v3/auth/tokens"
    APIport = KEYSTONEport
    url = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url)

    # Build the request body
    # body='{"auth":{"identity":{"methods":["password"],"password":{"user":{"name":"'+myusername+'","domain":{"name":"'+mydomainname+'"},"password":"'+mypassword+'"}}}}}'

    body = ('{'
    '   "auth": {'
    '       "identity": {'
    '           "methods": ['
    '               "password"'
    '           ],'
    '           "password": {'
    '               "user": {'
    '                   "domain": {'
    '                       "name": "default"'
    '                   },'
    '                   "name": "' + userName + '",'
    '                   "password": "' + myPassword + '"'
    '               }'
    '           }'
    '       },'
    '       "scope": {'
    '           "project": {'
    '               "domain": {'
    '                   "name": "default"'
    '               },'
    '               "name": "' + projectName + '"'
    '           }'
    '       }'
    '   }'
    '}')

    print("REQUEST BODY:", body)

    # Send the  POST request
    req = urllib.request.Request(url, body, headers)

    # quit()

    print("Read the response headers and body")

    # Read the response header
    header = urllib.request.urlopen(req).info()
    print("RESPONSE HEADER", header)

    # Read the response body
    response = urllib.request.urlopen(req).read()
    print("RESPONSE BODY", response)

    # quit()

    print("Decode the response header and body")
    print("------------------------------------")

    mytoken = header.getheader('X-Subject-Token')
    print("KEYSTONE TOKEN (X-Subject-Token)", mytoken)

    # Convert response body to pretty print format
    decoded = json.loads(response.decode('utf8'))
    pretty = json.dumps(decoded, sort_keys=True, indent=3)
    print("RESPONSE BODY IN PRETTY FORMAT", pretty)

    # Parse JSON formatted data for token issue date
    issued = decoded['token']['issued_at']
    print("TOKEN WAS ISSUED", issued)

    # Parse JSON formatted data for token expiration date
    expires = decoded['token']['expires_at']
    print("TOKEN WILL EXPIRE", expires)
    return mytoken;


def getAdminDetail():
   print("----------------Admin Details-------------------")
   return getTokenDetail("admin", "gkr1RDynOl6MCjpodlyKksFjSwL7Dlyl", "admin");


def getUserDetail(userName, password, projectName="admin"):
    print("----------------User Details-------------------")
    return getTokenDetail(userName, password, projectName);


def getAdminToken():
    print("----------------Admin Token-------------------")
    return getToken("admin", "gkr1RDynOl6MCjpodlyKksFjSwL7Dlyl", "admin");


def getUserToken(userName, password, projectName="admin"):
    print("----------------User Token-------------------")
    return getToken(userName, password, projectName);


import urllib.request, urllib.parse




def getAdminDetail():
    print("----------------Admin Details-------------------")
    return getTokenDetail("admin", "gkr1RDynOl6MCjpodlyKksFjSwL7Dlyl", "admin");


def getUserDetail(userName, password, projectName="admin"):
    print("----------------User Details-------------------")
    return getTokenDetail(userName, password, projectName);


def getAdminToken():
    print("----------------Admin Token-------------------")
    return getToken("admin", "gkr1RDynOl6MCjpodlyKksFjSwL7Dlyl", "admin");


def getUserToken(userName, password, projectName="admin"):
    print("----------------User Token-------------------")
    return getToken(userName, password, projectName);


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
