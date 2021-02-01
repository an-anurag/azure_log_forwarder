# Azure log forwarder


# What is this?

This is Azure log collector and forwarder. It collects all the Azure activity logs in realtime and 
stores in file and sends to UDP socket over syslog simultaneously.

# PREREQUISITES
-----------------------------------------------------------
1. Download and install Azure CLI with `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
2. Login into Azure CLI `az login`
3. Create role assignment by using `az ad sp create-for-rbac --name dev-sp-rbac --sdk-auth > local-sp.json`
4. `dev` can be any string in above command
5. Get the generated `local-sp.json` and store into `resource` directory.

# How to run?
-------------------------------------------------------------
2. Schedule running of `main.py` every 5 mins with crontab as follows
3. `*/5 * * * * python3 main.py`
4. This project is tested with python3 only.
