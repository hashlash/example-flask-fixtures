import unittest

from myapp import app
from myapp.models import db, Book, Author

from flask_fixtures import FixturesMixin

# Configure the app with the testing configuration
app.config.from_object('myapp.config.TestConfig')


# Make sure to inherit from the FixturesMixin class
class TestFoo(unittest.TestCase, FixturesMixin):
    # Specify the fixtures file(s) you want to load.
    # Change the list below to ['authors.yaml'] if you created your fixtures
    # file using YAML instead of JSON.
    fixtures = ['authors.json']

    # Specify the Flask app and db we want to use for this set of tests
    app = app
    db = db

    # Your tests go here

    def test_authors(self):
        authors = Author.query.all()
        assert len(authors) == Author.query.count() == 1
        assert len(authors[0].books) == 3

    def test_books(self):
        books = Book.query.all()
        assert len(books) == Book.query.count() == 3
        gibson = Author.query.filter(Author.last_name == 'Gibson').one()
        for book in books:
            assert book.author == gibson
