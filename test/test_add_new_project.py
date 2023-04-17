from model.MantisProject import Project

def test_add_new_project(app):
    app.session.login("administrator", "root")
    projects = Project(name="Test")
    old_projects = app.MantisProject.get_project_list()
    #projects = Project(name="Test")
    app.MantisProject.create_new_project(projects)
    new_projects = app.MantisProject.get_project_list()
    old_projects.append(projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

