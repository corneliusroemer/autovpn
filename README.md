# Autovpn: CLI tool for CISCO Anyconnect VPN

## Installation

```
pip install autovpn
```

## Usage

```
Usage: autovpn [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  configure   Configure VPN
  connect     Connect to VPN
  disconnect  Disconnect from VPN
  state       Show VPN state
```

## Configuration

You need to add a configuration file `~/.vpnconfig` to your home directory with the following content:
```
# Path to Cisco Anyconnect VPN binary
vpnpath = "/opt/cisco/anyconnect/bin/vpn" 

# Server to connect to
server = "vpn.mobile.unibas.ch"

# Username to connect with
username = "USERNAME" 

# Password to connect with
password = "PASSWORD" 
```
