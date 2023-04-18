from model.mantisproject import Project
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_new_project(app):
    app.session.ensure_login("administrator", "root")
    old_projects = app.soap.get_project_list()
    projects = Project(name=random_string("Test", 15))
    app.mantisproject.create_new_project(projects)
    new_projects = app.soap.get_project_list()
    old_projects.append(projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

