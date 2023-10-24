"""
Simple rest interface for VariantVlidator built using Flask Flask-RESTPlus and Swagger UI
"""

# Import modules
from flask import Flask,request, make_response
from flask_restx import Api, Resource, reqparse     
import requests
from dicttoxml import dicttoxml

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app", but I have had issues with this when it comes to deployment,
# so application is recommended
application = Flask(__name__)

# Define the API as api
api = Api(app = application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTPlus
# The first variable is the path of the namespace the second variable describes the space
hello_space = api.namespace('hello', description='Simple API that returns a greeting')
@hello_space.route("/")
class HelloClass(Resource):
    def get(self):
        return {
            "greeting": "Hello World"
        }


name_space = api.namespace('name', description='Return a name provided by the user')
@name_space.route("/<string:name>")
class NameClass(Resource):
    def get(self, name):
        return {
            "My name is" : name
        }


##########################################################################
#                                 Ex2                                    #
##########################################################################



@api.representation('text/xml')
def xml(data, code, headers):
    data = dicttoxml(data)
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'text/xml'
    return resp



# Slightly confused about exercise two, this was my attempt at it, calling an
# external api to be repeated locally?
vv_space = api.namespace('VariantValidator', description='VariantValidator APIs')
@vv_space.route("/variantvalidator_external")
class VariantValidatorClass(Resource):
    def get(self):
        
        url = "https://rest.variantvalidator.org/hello/"
        
        res = requests.get(url)
         
        validation = res.headers
        content = res.json()
        return content


vv_space = api.namespace('return_hgvs_refs', description='VariantValidator APIs')
@vv_space.route("/variantvalidator_external_refs/<string:hgvs>")
class VariantValidatorClass2(Resource):
    def get(self,hgvs): 
        
        url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts/"
        

        #if (request.headers.get('accept') == "application/json"):
            
         #   url = url + hgvs 

        url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts/" + hgvs
        validation = requests.get(url)
        content = validation.json()
        return content
         
        #return content 







# Allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True # Enable debugging mode
    application.run(host="127.0.0.1", port=5000) # Specify a host and port fot the app          