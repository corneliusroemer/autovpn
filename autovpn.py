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
    return parse_config_file(f'{os.path.expanduser("~")}/.autovpnconfig')

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
    settings = get_config_dict()
    settings['vpnpath'] = click.prompt(f'Enter VPN binary path', default=settings['vpnpath'], type=str)
    settings['server'] = click.prompt(f'Enter VPN server', default=settings['server'], type=str)
    settings['username'] = click.prompt(f'Enter VPN username', default=settings['username'], type=str)
    settings['password'] = click.prompt(f'Enter VPN password', default=settings['password'], show_default = False, type=str)
    with open(f'{os.path.expanduser("~")}/.autovpnconfig', 'w') as f:
        f.write(toml.dumps(settings))
    click.echo(f'Config file saved to {os.path.expanduser("~")}/.autovpnconfig')


# TODO: Kill anyconnect UI
# TODO: Multiple servers