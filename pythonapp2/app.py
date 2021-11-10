#Consumer app
from mask import Mask
from mask.parse import pre, Rule

app = Mask(__name__)


rule = {
    "name": Rule(type=str, gte=2, dest="Name")
}

@app.route("/testpythonapps", methods=['POST'])
def incoming():
    print("Hello from Kafka!", flush=True)
    data = request.get_json()
    print(data, flush=True)
    return(data)


if __name__ == "__main__":
    # run the flask app 
    app.run(port=3000, debug=True) # run on the server
    # app.run(debug=True)  # run localy
