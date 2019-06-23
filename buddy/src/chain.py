# chain.py stores all the data revisions for each day in parent-child relation.
import os
import errno
import click

indexsize = 24
# In index field we store following information:
# hash(date): 8 bytes
# offset: 4 bytes
# hunksize: 4 bytes
# parent: 8 bytes

class chain(object):
    """Storage backend"""

    def __init__(self, date=None):
        self.base = None
        self.top = None
        self.home = os.getenv('HOME')
        self.store = self.home + '/.work/data/'
        # index = ['dd', 'dd', 'dd', 'dd', 'dd', dd']
        self.index = []
        # metadata = { 'date': ['data','off', 'size', 'par']
        self.metadata = {}
        if not os.path.isdir(self.store):
            try:
                os.makedirs(self.store)
            except OSError:
                click.secho('creation of %s failed!'.format(self.store),
                            fg='red')

    def addhunk(self, text, date):

        # print(date)
        assert len(date) <= 8 #ddmmyyyy
        self.indexfile = self.store + date[2:8] + '.d'
        indexdata = ''
        try:
            with open(self.indexfile, 'rb') as f:
                indexdata = f.read()
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise

        # if indexdata:
            # # indexfile exists, find the offset where to insert data
            # self.loadindex()
            # off, size = findoffset()
        # else:
        # no indexfile, let's create a new one
        click.secho('creating a new indexfile!', fg='green')
        with open(self.indexfile, 'w+') as f:
            offset = '0016'
            hunksize = len(text)
            parent = '00000000'
            data = date + offset + str(hunksize) + parent + text
            entry = (data)
            f.write(entry)


    def getdaytext(self, date):
        return ''
    def parseindex(self, index):
        pass
    def loadindex(self, indexfile):
        indexdata = ''
        with open(indexfile, 'rb') as f:
            indexdata = f.read()
        data = parseindex(indexdata)
        self.index, self.metadata = data
