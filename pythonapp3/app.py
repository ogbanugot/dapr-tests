from dapr.ext.grpc import App, BindingRequest
from dapr.clients import DaprClient
import json

app = App()

@app.binding('testpythonapps')
def binding(request: BindingRequest):
    print(request.text(), flush=True)
    with DaprClient() as d:
        response = d.invoke_method(
            'teambyocr',
            'teambyocr',
            data=json.dumps(request.text()),
        )
    print(response)

if __name__ == "__main__":
    app.run(50059) # run on the server
