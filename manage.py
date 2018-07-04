import unittest

from myapp import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def tests():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('myapp/fixtures', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
