from azure_log_forwarder import AzureLogForwarder


def main():
    az = AzureLogForwarder()
    az.forward()


if __name__ == '__main__':
    main()
