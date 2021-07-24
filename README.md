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
In order to let `autovpn` know about your VPN server and credentials, you need to configure it once. You can do so in two ways: Either by running `autovpn configure` or by adding a config file `~/.autovpnconfig` to your home directory with the following content:
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

The command `autovpn configure` automatically creates the config file if it doesn't exist and overwrites any existing one.
