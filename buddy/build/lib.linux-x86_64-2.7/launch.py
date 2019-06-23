import click
import datetime

from chain import chain
from . import util

markers = {'commit': ("\n\n# Write here to save the work summary of the day.\n"
                      "# These commentted lines will not be stored with your commit.\n"
                     ),
           'update': ''}

@click.group(invoke_without_command=True)
@click.option('-v', '--verbose', help='enable verbose mode',
               is_flag=True, flag_value=True)
def work(verbose):
    '''
    I am your friend; who knows all about your work.
    '''
    if verbose:
        click.echo("we are in verbose mode")

    
@work.command()
def commit(date=None):
    """Make a commit of your work."""

    if date is None:
        date = util.getdate()
    else:
        date = parsedate(date)

    # idx = chain[monthyear]
    monthchain = chain()
    oldcontent = monthchain.getdaytext(date)
    data = click.edit(oldcontent + markers['commit'])
    entry = ''
    if data is not None:
        entry = data.split(markers['commit'], 1)[0].rstrip()
    # store the data entry
    monthchain.addhunk(entry, date)

@work.command()
def log():
    '''
    show the graph of your work history.
    '''
    click.echo("lets update your work")
    
@work.command()
def update():
    '''
    update your work
    '''
    click.echo("lets update your work")

#if __name__ == '__main__':
#    work()
