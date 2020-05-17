from Config import Config

class ConfigStub(Config):

    def getConfig(self):
        dataSourceFields = []
        dataSourceFields.append('derek.somerville@glasgow.ac.uk')
        dataSourceFields.append('Derek')
        dataSourceFields.append('Somerville')
        dataSourceFields.append('1234')
        return dataSourceFields