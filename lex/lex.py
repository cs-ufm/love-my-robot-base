from flask import Flask
import redis, json

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe("test")


@app.route("/")
def index():
    return "Hello from Flask!"

def subJSON():
    """Reads message to JSON.

    Reads constantly if there's any new message 
    in the channel, if so it parses it into
    a JSON format and returns it.
    """
    json_message = None
    print("Running subJSON()")
    for message in p.listen():
        print(f"message.get(data):{message.get('data')}") # DELETE LATER
        message_data = message.get('data')

        if not isinstance(message_data, int):
            print("\nIF PASSED")
            json_string = message.get('data') # DELETE LATER
            print(f"json_string:{json_string}")
            
            json_message = json.loads(json_string)
            print(f"json.get(name):{json_message.get('name')}")
        print(f"message: {message}") # DELETE LATER 
    return json_message

new_json = subJSON()

# print(f"new_json.get('name'):{new_json.get('name')}")
print(type(new_json))

if __name__ == "__main__":
    app.run(host="0.0.0.0")



