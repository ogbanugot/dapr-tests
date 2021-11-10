#Consumer app
from mask import Mask
from mask.parse import pre, Rule
from hello_pb2 import HelloResponse
app = Mask(__name__)


@app.route(method="testpythonapps", service="Hello")
def incoming(request, context):
    print("Hello from Kafka!", flush=True)
    #params = pre.parse(rule=rule, request=request, context=context)
    data = HelloResponse(message=request)
    print(data, flush=True)
    return(data)


if __name__ == "__main__":
    # run the flask app 
    app.run(port=3000, debug=True) # run on the server
    # app.run(debug=True)  # run localy
