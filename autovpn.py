import os
import click
from subprocess import Popen, PIPE
from sortedcontainers import SortedSet
import toml

def parse_config_file(path):
    """Parse TOML config file and return dictionary"""
    try:
        with open(path, 'r') as f:
            return toml.loads(f.read())
    except:
        open(path,'a').close() 
        return {}

def get_config_dict():
    return parse_config_file(f'{os.path.expanduser("~")}/.autovpnconfig')

@click.group()
def cli():
    pass

@cli.command()
def connect():
    """Connect to VPN"""
    settings = get_config_dict()
    if settings == {}:
        click.echo('autovpn has not been configured\nPlease configure using `autovpn configure`')
        return
    click.echo('Connecting to VPN...')
    with Popen([settings['vpnpath'],'connect',settings['server'],'-s'],stdin=PIPE,stdout=PIPE,text=True) as proc:
        (stdout,stderr) = proc.communicate(f'{settings["username"]}\n{settings["password"]}\ny')
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN>' not in x, output))
    click.echo('\n'.join(SortedSet(output)))

@cli.command()
def state():
    """Show VPN state"""
    settings = get_config_dict()
    if settings == {}:
        click.echo('autovpn has not been configured\nPlease configure using `autovpn configure`')
        return
    with Popen([settings['vpnpath'],'state'],stdout=PIPE,text=True) as proc:
        stdout = proc.stdout.read()
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN' not in x, output))
    click.echo('\n'.join(output))

@cli.command()
def disconnect():
    """Disconnect from VPN"""
    settings = get_config_dict()
    if settings == {}:
        click.echo('autovpn has not been configured\nPlease configure using `autovpn configure`')
        return
    with Popen([settings['vpnpath'],'disconnect'],stdout=PIPE,text=True) as proc:
        stdout = proc.stdout.read()
    output = stdout.split("\n")
    output = list(filter(None, output))
    output = list(filter(lambda x: 'VPN' not in x, output))
    click.echo('\n'.join(output))

@cli.command()
def configure():
    """Configure VPN"""
    settings = get_config_dict()
    settings['vpnpath'] = click.prompt(f'Enter VPN binary path', default=settings.get('vpnpath','/opt/cisco/anyconnect/bin/vpn'), type=str)
    settings['server'] = click.prompt(f'Enter VPN server', default=settings.get('server','vpn.mobile.unibas.ch'), type=str)
    settings['username'] = click.prompt(f'Enter VPN username', default=settings.get('username'), type=str)
    settings['password'] = click.prompt(f'Enter VPN password {"[hidden]" if "password" in settings else ""}', default=settings.get('password'), hide_input=True, show_default = False, type=str)
    with open(f'{os.path.expanduser("~")}/.autovpnconfig', 'w') as f:
        f.write(toml.dumps(settings))
    click.echo(f'Configuration saved to {os.path.expanduser("~")}/.autovpnconfig')


# TODO: Kill anyconnect UI
# TODO: Multiple servers