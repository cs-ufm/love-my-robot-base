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
    """Converts message string to JSON.

    Once invoked through subGET() it handles
    the message by converting it from string
    to JSON and assigns it to 'global_json'
    """
    print("\nRan: message_handler()")
    print(f"MY HANDLER: '{message.get('data')}")

    message_data = message.get('data')

    if message_data:
        print("\nIF PASSED")
        # json_string = message.get('data')
        # print(f"json_string:{json_string}") # DELETE LATER 
        
        json_message = json.loads(message_data)
        print(f"json.get(name):{json_message.get('name')}") # DELETE LATER 
        # print(f"message: {message}") # DELETE LATER 
        global_json = json_message



def subGET():
    """Subscribes to channel and sends message 
    to handler.

    When in need of reading messages this is the 
    function call. Once called it will subscribe 
    asyncronously to channel (where channel = 'CHANNEL_NAME' 
    defined on the first lines of this file).

    p.run_in_thread(): Behind the scenes, this is
    simply a wrapper around get_message() that runs 
    in a separate thread, and use asyncio.run_coroutine_threadsafe() 
    to run coroutines.

    Coroutine: Coroutines are generalization of subroutines. 
    They are used for cooperative multitasking where a process 
    voluntarily yield (give away) control periodically or when 
    idle in order to enable multiple applications to be run 
    simultaneously.
    """
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
    
    




