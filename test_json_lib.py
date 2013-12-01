import openerplib

connection = openerplib.get_connection(hostname="192.168.0.11", port=8090,  database="test", \
    login="admin", password="admin", protocol="jsonrpc")
user_model = connection.get_model("res.users")
ids = user_model.search([("login", "=", "admin")])
user_info = user_model.read(ids[0], ["name"])
print user_info["name"]