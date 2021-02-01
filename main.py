from azure_log_forwarder import AzureLogForwarder
from config_reader import conf

HOST = conf.read('syslog', 'host')
PORT = conf.read('syslog', 'port')
OUTFILE = conf.read('log-file', 'name')


def main():
    az = AzureLogForwarder(host=HOST, port=PORT, outfile=OUTFILE)
    az.run()


if __name__ == '__main__':
    main()
