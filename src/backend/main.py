from server import Server
import time

def main(server:Server):
    while(True):
        try:
            time.sleep(1)
            server.publish_action(action=1)
        except:
            break
    server.disconnect()

if __name__ == "__main__":
    server = Server()
    main(server)