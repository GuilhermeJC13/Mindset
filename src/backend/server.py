import paho.mqtt.client as mqtt
import constants

class Server():
    
    def __init__(self):
        self.client = self.connect()

    def connect(self):
        client = mqtt.Client()

        client.connect(constants.BROKER_ADRESS, port=constants.PORT)
        client.loop_start()

        print("Connected to MQTT broker!")

        return client

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

        print("Disconnected to MQTT broker!")

    def publish_action(self, action):
        result = self.client.publish(constants.TOPIC, action)
        status = result[0]
        if status == 0:
            print(f"Sent '{action}' to the topic '{constants.TOPIC}'")
        else:
            print(f"Failed to send action to the topic '{constants.TOPIC}'")