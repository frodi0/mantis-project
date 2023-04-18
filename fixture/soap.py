
from suds.client import Client
from suds import WebFault
from model.mantisproject import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config["webadmin"]["username"]
        password = self.app.config["webadmin"]["password"]
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            accessible_projects = self.convert_projects_to_model(list(client.service.mc_projects_get_user_accessible(username, password)))
            return accessible_projects
        except WebFault:
            return False

    def convert_projects_to_model(self, accessible_projects):
        def convert(mantisproject):
            return Project(id=str(mantisproject.id), name=mantisproject.name)
        return list(map(convert, accessible_projects))



