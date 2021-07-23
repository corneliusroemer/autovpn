import os
import click
from subprocess import Popen, PIPE
from sortedcontainers import SortedSet
import toml

def parse_config_file(path):
    """Parse TOML config file and return dictionary"""
    with open(path, 'r') as f:
        return toml.loads(f.read())

def get_config_dict():
    return parse_config_file(f'{os.path.expanduser("~")}/.vpnconfig')

@click.group()
def cli():
    pass

@cli.command()
def connect():
    """Connect to VPN"""
    settings = get_config_dict()
    with Popen(['/opt/cisco/anyconnect/bin/vpn','connect',settings['server'],'-s'],stdin=PIPE,stdout=PIPE,text=True) as proc:
        (stdout,stderr) = proc.communicate(f'{settings["username"]}\n{settings["password"]}\ny')
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN>' not in x, output))
    click.echo('\n'.join(SortedSet(output)))

@cli.command()
def state():
    """Show VPN state"""
    with Popen(['/opt/cisco/anyconnect/bin/vpn','state'],stdout=PIPE,text=True) as proc:
        stdout = proc.stdout.read()
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN' not in x, output))
    click.echo('\n'.join(output))

@cli.command()
def disconnect():
    """Disconnect from VPN"""
    with Popen(['/opt/cisco/anyconnect/bin/vpn','disconnect'],stdout=PIPE,text=True) as proc:
        stdout = proc.stdout.read()
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN' not in x, output))
    click.echo('\n'.join(output))

@cli.command()
def configure():
    """Configure VPN"""


# TODO: Kill anyconnect UI
# TODO: Check state first
# TODO: login/logout
# TODO: Configuration