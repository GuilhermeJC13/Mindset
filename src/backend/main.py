from server import Server
import time

def main(server:Server):
    time.sleep(1)
    server.publish_action(action=1)
    time.sleep(5)
    server.publish_action(action=0)
    time.sleep(5)
    server.publish_action(action=2)
    server.disconnect()

if __name__ == "__main__":
    server = Server()
    main(server)