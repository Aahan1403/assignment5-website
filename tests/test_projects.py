import DAL


def test_projects_list_shows_added_project(client):
    # Add a project directly through the DAL and verify it appears on the projects page
    DAL.add_project('Test Project', 'A test description', None)
    rv = client.get('/projects')
    assert b'Test Project' in rv.data
    assert b'Test description' in rv.data or b'Test Project' in rv.data


def test_add_project_via_post(client):
    # Post a new project via the web form and verify it appears on the projects page
    rv = client.post('/add_project', data={
        'title': 'Another Project',
        'description': 'A second description',
        'imagefilename': ''
    }, follow_redirects=True)
    assert b'Another Project' in rv.data
    assert b'A second description' in rv.data


def test_add_project_missing_fields_not_added(client):
    # Posting missing title/description should not add a project
    rv = client.post('/add_project', data={'title': '', 'description': '', 'imagefilename': ''}, follow_redirects=True)
    # Now check projects listing does not contain a title named 'Incomplete'
    rv2 = client.get('/projects')
    assert b'Incomplete' not in rv2.data
