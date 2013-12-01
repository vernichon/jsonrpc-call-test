from  openerp_jsonrpc_client import *
OE_BASE_SERVER_URL = "http://192.168.0.11:8090"
server = OpenERPJSONRPCClient(OE_BASE_SERVER_URL)
session_info = server.session_authenticate('test', 'admin', 'admin', OE_BASE_SERVER_URL)

try:
    res_users_obj = server.get_model('res.users')
    user = res_users_obj.read([1], ['login', 'password'])
    print user
except OpenERPJSONRPCClientException as exc:
    print "message: %s" % exc.message
    print "data: %s" % exc.data
    print "data.type: %s" % exc.data['type']
    print "data.fault_code: %s" % exc.data['fault_code']
    raise exc
    