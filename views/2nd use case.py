
from connect import *

####################################################################
##########Creation#############
def createNewProject(mytoken, projectName, projectDescription, domainId):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)
    body = ('{'
    '"project": {'
    '    "description": "' + projectDescription + '",'
    '    "domain_id": "' + domainId + '",'
    '    "enabled": true,'
    '    "is_domain": false,'
    '    "name": "' + projectName + '"'
    '}'
    '}')

    # Build the request URL
    CMDpath = "/v3/projects"
    APIport = KEYSTONEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, body, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)
    return decoded1;

# create a new project
def createNewUser(mytoken, userName, password, domainId, projectId):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)
    body = ('{'
    '"user": {'
    '    "default_project_id": "' + projectId + '",'
    '    "domain_id": "' + domainId + '",'
    '    "enabled": true,'
    '    "name": "' + userName + '",'
    '    "password": "' + password + '"'
    '}'
    '}')

    # Build the request URL
    CMDpath = "/v3/users"
    APIport = KEYSTONEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("REQUEST URL:", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, body, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)
    return decoded1['user']['id'];


def addNewUserToProject(mytoken, userId):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              # 'Accept'         :   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    # print "REQUEST BODY:" ; print body
    # print"--------------------------------------------------------------------------"
    # print "" ; print ""

    # Build the URL
    # /v3/projects/{project_id}/users/{user_id}/roles/{role_id}
    CMDpath = "/v3/projects/" + "65a1fb5b49aa49a8a82ee57db2ca38fa" + \
        "/users/" + userId + "/roles/" + "e3b28881878942c2a0b6447059cb1d8b"
    APIport = KEYSTONEport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, None, headers)

    try:
        response1 = urllib.request.urlopen(req1).read()
        print("action execution successful")
        return {"status": "OK", "message": "success"};
    except Exception as e:
        print("This is an exception")
        print(str(e))
        return {"status": "ERROR", "message": str(e)};


# create a new server
def createNewServer(mytoken, vmName, flavorId, imageId, networkId):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              'Accept':   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)

    body = ('{'
    '"server": {'
    '   "name": "' + vmName + '",'
    '    "imageRef": "' + imageId + '",'
    '    "flavorRef": "' + flavorId + '",'
    '    "networks": ['
    '        {'
    '            "uuid": "' + networkId + '"'
    '        }'
    '    ]'
    '}'
    '}')
    # Build the URL
    CMDpath = "/v2.1/servers"
    APIport = NOVAport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, body, headers)

    # Read the response
    response1 = urllib.request.urlopen(req1).read()

    # Convert to JSON format
    decoded1 = json.loads(response1.decode('utf8'))

    # Make it look pretty and indented
    pretty1 = json.dumps(decoded1, sort_keys=True, indent=3)
    print("RESPONSE (FORMATTED)", pretty1)
    return decoded1;



###################################################################"


###################Crud for instances##################"
def instanceAction(mytoken, instanceId, action):
    # mytoken = getAdminToken()

    # Build the headers

    headers = {
              'Content-Type':   'application/json',
              # 'Accept'         :   'application/json',
              'X-Auth-Token':    mytoken
               }
    print("REQUEST HEADERS", headers)
    body = ('{'
    '"'+action+'":null'
    '}')

    print("REQUEST BODY:", body)

    # Build the URL
    # http://localhost:8774/v2.1/servers/6269d835-bee0-49b7-ba1c-f348aac88d1c/action
    CMDpath = "/v2.1/servers/"+instanceId+"/action"
    APIport = NOVAport
    url1 = "http://"+hostIP+":"+APIport+CMDpath
    print("URL", url1)

    # Send the GET request
    # Note that the second parameter which normally carries the body data
    # is "None", making the request a "GET" instead of a "POST"
    req1 = urllib.request.Request(url1, body, headers)

    try:
        response1 = urllib.request.urlopen(req1).read()
        print("action execution successful")
        return {"status": "OK", "message": "success"};
    except Exception as e:
        print("This is an exception")
        print(str(e))
        return {"status": "ERROR", "message": str(e)};


def startInstance(mytoken, instanceId):
    print("start instance")
    return instanceAction(mytoken, instanceId, "os-start");


def stopInstance(mytoken, instanceId):
    print("stop instance")
    return instanceAction(mytoken, instanceId, "os-stop");


def pauseInstance(mytoken, instanceId):
    print("pause instance")
    return instanceAction(mytoken, instanceId, "pause");


def unpauseInstance(mytoken, instanceId):
    print("unpause instance")
    return instanceAction(mytoken, instanceId, "unpause");


def suspendInstance(mytoken, instanceId):
    print("suspend instance")
    return instanceAction(mytoken, instanceId, "suspend");


def resumeInstance(mytoken, instanceId):
    print("resume instance")
    return instanceAction(mytoken, instanceId, "resume");


def deleteInstance(mytoken, instanceId):
    print("forceDelete instance")
    return instanceAction(mytoken, instanceId, "forceDelete");


######################################################################""
############################Panne HW########################################

def Model de redondance