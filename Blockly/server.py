import http.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys
sys.path.append('..')
import mBot.interfaces.setMotorPower as RobotMotorPower 


def registerRobotXmlRpcMethods(server):
    
    # Register standard XML-RPC methods.
    server.register_introspection_functions()
    
    # Register the motor power command function.
    RobotMotorPower.init()
    server.register_function(RobotMotorPower.set,'setRobotMotorPower')


    
    
# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, http.server.SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        http.server.SimpleHTTPRequestHandler.do_GET(self)      
    
    
    
    
# Start running the server ...    
if __name__ == "__main__":
    
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer(("", port), RequestHandler)
    
    # Register the XML-RPC methods ...
    registerRobotXmlRpcMethods(server)
    
    # Start to server.
    server.serve_forever()
