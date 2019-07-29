import LinuxShell
import config
import threading

def run():
    shell = LinuxShell.LinuxShell(config.SERVER_IP, config.SERVER_PORT)

    try:
        connection_thread = threading.Thread(name='Connection', target=shell.connect, args=())
        connection_thread.start()
    except KeyboardInterrupt as e:
        pass




if __name__ == '__main__':
    run()
