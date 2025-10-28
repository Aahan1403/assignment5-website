import pytest
import importlib
import DAL


@pytest.fixture
def client(tmp_path):
    """Create a Flask test client that uses a temporary SQLite DB.

    We set DAL.DB_PATH to a temporary file before importing the app so
    the application's init_db() uses the test database.
    """
    test_db = tmp_path / "test_projects.db"
    DAL.DB_PATH = str(test_db)

    # Import the app after setting DAL.DB_PATH so the app initializes the test DB
    app_module = importlib.import_module('app')

    # Ensure table exists
    DAL.init_db()

    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client
