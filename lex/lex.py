from flask import Flask
import redis, json, threading, time, asyncio

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub(ignore_subscribe_messages=True)

channel = 'test'

global_json = None
message = None

@app.route("/")
def index():
    return "Hello from Flask!"


def message_handler(message):
    print("\nRan: message_handler()")
    print(f"MY HANDLER: '{message['data']}")
    # """Reads message to JSON.

    # Reads constantly if there's any new message 
    # in the channel, if so it parses it into
    # a JSON format and returns it.
    # """
    # print("\nRan: message_handler()")
    # print('MY HANDLER: ', message['data'])
    # message_data = message.get('data')

    # if not isinstance(message_data, int):
    #     # print("\nIF PASSED")
    #     json_string = message.get('data')
    #     # print(f"json_string:{json_string}") # DELETE LATER 
        
    #     json_message = json.loads(json_string)
    #     # print(f"json.get(name):{json_message.get('name')}") # DELETE LATER 
    #     # print(f"message: {message}") # DELETE LATER 
    #     global_json = json_message



def subGET():
    p.subscribe(**{channel: message_handler})
    thread = p.run_in_thread(sleep_time=0.1, daemon=True)
    print("\nsubGET(): Ran: subGET()")
    message = p.get_message()
    print(f"subGET: message: {message}")
    # json_message = None
    # print("Running subJSON()")
    # for message in p.listen():
    #     # print(f"message.get(data):{message.get('data')}") # DELETE LATER
    #     message_data = message.get('data')


# new_json = subJSON()

# print(f"new_json.get('name'):{new_json.get('name')}")
# print("NOT BLOCKING")

if __name__ == "__main__":
    subGET()
    if global_json:
        print(f"global_json.get('name'):{global_json.get('name')}")
    app.run(host="0.0.0.0")
    # asyncio.run(subJSON())
    # print("NOT BLOCKING")
    
    




