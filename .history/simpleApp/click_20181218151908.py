import click

from home.home.py import startApp
@click.group()
def cli():
    pass

@cli.command()
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()