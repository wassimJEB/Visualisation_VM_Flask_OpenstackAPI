from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import render_template, json, request, session
from views.Visualisation import *
from views.connect import *
import openstack

# determine route
application = Flask(__name__)

application.secret_key = 'secret'
client = MongoClient('mongodb:openstack')

db = client.MachineData
adminInfo = getAdminDetail()
mytoken = adminInfo['token']
myDomainId = adminInfo['domainId']
myProjectId = adminInfo['projectID']
# mytoken = openstack.getAdminToken()

myFlavorInfo = openstack.listOfFlavors(mytoken)
myImageInfo = openstack.listOfImages(mytoken)
myNetworkInfo = openstack.listOfNetworks(mytoken)



def myGetImageNameById(imageId):
    for image in myImageInfo['images']:
        tempImageId = image['id']
        if imageId == tempImageId:
            return image['name']
    return "not found"


def myGetFlavorNameById(flavorId):
    for flavor in myFlavorInfo['flavors']:
        tempFlavorId = flavor['id']
        if flavorId == tempFlavorId:
            return flavor['name']
    return "not found"


#########################START#################################################
@application.route('/')
@application.route('/logout')
def home():
    return render_template('index.html')


@application.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@application.route('/machine')
def machine():
    return render_template('machine.html')


@application.route('/profile')
def profile():
    return render_template('profile.html')


@application.route('/list')
def showMachineList1():
    return render_template('instances.html')


@application.route('/billing')
def billing():
    return render_template('billing.html')


@application.route('/flavors')
def flavors():
    return render_template('flavors.html')


@application.route('/images')
def images():
    return render_template('images.html')


@application.route('/network')
def network():
    return render_template('network.html')


@application.route("/getUserlist", methods=['POST'])
def getUserList():
    try:

        username = request.json['user']
        password = request.json['pass']
        machinelist = db.userlist.find({})

        message = ""
        for machine in machinelist:
            print(machine)
            if (machine['username'] == username and machine['password'] == password):
                message = 'successful'
                break;

        if (message == 'successful'):
            print('successful')
            session['username'] = username
            return 'successful'
        else:
            print('unsuccessful')
            return 'unsuccessful'
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/sessiondestroy", methods=['POST'])
def sessiondestroy():
    try:
        # session.clear()
        session.pop('username', None)
        print('session destroy - done')
        return 'done'
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/sessioncheck", methods=['POST'])
def sessioncheck():
    if (session['username'] != None):
        print(session['username'])
        return session['username']
    else:
        return 'not exist'


@application.route("/addUser", methods=['POST'])
def addUser():
    try:
        username = request.json['user']
        password = request.json['pass']
        domain = request.json['domainame']
        db.userlist.insert_one({
            'domain': domain, 'username': username, 'password': password
        })
        return jsonify(status='OK', message='inserted successfully')

    except Exception as e:
        import logging
        logging.exception('Error')
        return jsonify(status='ERROR', message=str(e))


@application.route("/getUserProfile", methods=['POST'])
def getUserProfile():
    try:
        userlist = ""
        print('profile')
        username = request.json['profile']
        userlist = db.userlist.find_one({'username': username})

        data = [
            userlist['username'],
            userlist['password'],
            userlist['domain']
        ]
        return json.dumps(data)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route('/getMachine', methods=['POST'])
def getMachine():
    try:
        machineId = request.json['id']
        machine = db.Machines.find_one({'_id': ObjectId(machineId)})
        machineDetail = {
            'device': machine['device'],
            'ip': machine['ip'],
            'username': machine['username'],
            'password': machine['password'],
            'port': machine['port'],
            'id': str(machine['_id'])
        }
        return json.dumps(machineDetail)
    except Exception as e:
        return str(e)


@application.route('/updateMachine', methods=['POST'])
def updateMachine():
    try:
        machineInfo = request.json['info']
        machineId = machineInfo['id']
        device = machineInfo['device']
        ip = machineInfo['ip']
        username = machineInfo['username']
        password = machineInfo['password']
        port = machineInfo['port']

        db.Machines.update_one({'_id': ObjectId(machineId)}, {
            '$set': {'device': device, 'ip': ip, 'username': username, 'password': password, 'port': port}})
        return jsonify(status='OK', message='updated successfully')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


def getServerIpAddress(networkAddr):
    netKeys = networkAddr.keys()
    for key in netKeys:
        for netId in networkAddr[key]:
            return netId['addr']


@application.route("/getMachineList", methods=['POST'])
def getMachineList():
    try:
        serverInfo = openstack.listOfServer(mytoken)
        # flavorInfo = openstack.listOfFlavors(mytoken)
        # imageInfo = openstack.listOfImages(mytoken)
        # networkInfo = openstack.listOfNetworks(mytoken)
        flavorInfo = myFlavorInfo
        imageInfo = myImageInfo
        networkInfo = myNetworkInfo

        machineList = []
        flavorList = []
        imageList = []
        networkList = []
        for server in serverInfo['servers']:
            imageId = server['image']['id']
            imageName = myGetImageNameById(imageId)
            flavorId = server['flavor']['id']
            flavorName = myGetFlavorNameById(flavorId)
            networkAddr = server['addresses']
            ipAddress = getServerIpAddress(networkAddr)
            machineItem = {
                'name': server['name'],
                'image_name': imageName,
                'ip_address': ipAddress,
                'flavor': flavorName,
                'status': server['status'],
                'zone': server['OS-EXT-AZ:availability_zone'],
                'task': server['OS-EXT-STS:task_state'],
                'id': server['id']
            }
            machineList.append(machineItem)

        for flavor in flavorInfo['flavors']:
            flavorItem = {'name': flavor['name'], 'id': flavor['id']}
            flavorList.append(flavorItem)

        for image in imageInfo['images']:
            imageItem = {'name': image['name'], 'id': image['id']}
            imageList.append(imageItem)

        for network in networkInfo['networks']:
            networkItem = {'name': network['name'], 'id': network['id']}
            networkList.append(networkItem)

        stackInfo = {'servers': machineList, 'flavors': flavorList, 'images': imageList, 'networks': networkList}
    except Exception as e:
        return str(e)
    return json.dumps(stackInfo)


@application.route("/getFlavorList", methods=['POST'])
def getFlavorList():
    try:
        flavorInfo = myFlavorInfo
        flavorList = []
        for flavor in flavorInfo['flavors']:
            flavorItem = {
                'name': flavor['name'],
                'ram': flavor['ram'],
                'isPublic': flavor['os-flavor-access:is_public'],
                'vcpus': flavor['vcpus'],
                'disk': flavor['disk'],
                'id': flavor['id']
            }
            flavorList.append(flavorItem)

    except Exception as e:
        return str(e)
    return json.dumps(flavorList)


@application.route("/getImageList", methods=['POST'])
def getImageList():
    try:
        imageInfo = myImageInfo
        imageList = []
        for image in myImageInfo['images']:
            imageItem = {
                'name': image['name'],
                'status': image['status'],
                'minDisk': image['min_disk'],
                'minRam': image['min_ram'],
                'size': image['size'],
                'id': image['id']
            }
            imageList.append(imageItem)

    except Exception as e:
        return str(e)
    return json.dumps(imageList)


@application.route("/getNetworkList", methods=['POST'])
def getNetworkList():
    try:
        networkInfo = myNetworkInfo
        netList = []
        for network in networkInfo['networks']:
            netItem = {
                'name': network['name'],
                'status': network['status'],
                'shared': network['shared'],
                'type': network['provider:network_type'],
                'id': network['id']
            }
            netList.append(netItem)

    except Exception as e:
        return str(e)
    return json.dumps(netList)


@application.route("/getServerUsage", methods=['POST'])
def getServerUsage():
    try:
        usageInfo = openstack.getServerUsage(mytoken, myProjectId)
        serverUsageInfo = usageInfo['tenant_usage']['server_usages']
        usageList = []
        for usage in serverUsageInfo:
            usageItem = {
                'name': usage['name'],
                'uptime': usage['uptime'],
                'memory': usage['memory_mb'],
                'state': usage['state'],
                'id': usage['instance_id']
            }
            usageList.append(usageItem)

    except Exception as e:
        return str(e)
    return json.dumps(usageList)

@application.route("/addMachine", methods=['POST'])
def addMachine():
    try:
        json_data = request.json['info']
        instanceName = json_data['instanceName']
        flavorId = json_data['flavor']['id']
        imageId = json_data['image']['id']
        networkId = json_data['network']['id']
        print(instanceName)
        print(flavorId)
        print(imageId)
        print(networkId)
        openstack.createNewServer(mytoken, instanceName, flavorId, imageId, networkId)
        db.Machines.insert_one({
            'device': instanceName, 'ip': flavorId, 'username': imageId, 'password': networkId, 'port': networkId
        })
        return jsonify(status='OK', message='inserted successfully')

    except Exception as e:
        return jsonify(status='ERROR', message=str(e))

@application.route("/deleteMachine", methods=['POST'])
def deleteMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.deleteInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


# added by abhijeet (remove comment later on)

@application.route("/resumeMachine", methods=['POST'])
def resumeMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.resumeInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/suspendMachine", methods=['POST'])
def suspendMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.suspendInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/unpauseMachine", methods=['POST'])
def unpauseMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.unpauseInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/pauseMachine", methods=['POST'])
def pauseMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.pauseInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/stopMachine", methods=['POST'])
def stopMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.stopInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route("/startMachine", methods=['POST'])
def startMachine():
    try:
        machineId = request.json['id']
        print(machineId)
        response = openstack.startInstance(mytoken, machineId)
        return jsonify(response)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))



@application.route('/Maintenance ',methods=['GET','POST'])
def Maintenance():


    return render_template('Maintenance.html')
# start this web serevr
if __name__ == "__main__":
    application.run(host='127.0.0.1', port=5010)