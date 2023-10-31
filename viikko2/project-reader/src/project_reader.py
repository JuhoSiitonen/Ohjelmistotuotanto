from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        #print(parsed_toml)
        name = parsed_toml['tool']['poetry']['name']
        desc = parsed_toml['tool']['poetry']['description']
        depenc = parsed_toml['tool']['poetry']['dependencies']
        dev = parsed_toml['tool']['poetry']['group']['dev']['dependencies']
        auth = parsed_toml['tool']['poetry']['authors']
        lic = parsed_toml['tool']['poetry']['license']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depenc, dev, auth, lic)
