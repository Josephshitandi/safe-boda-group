from app import create_app,db
from flask_script import Manager,Server
<<<<<<< HEAD
from app.models import Rider
=======
from app.models import Book,User,Role
>>>>>>> dev
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
<<<<<<< HEAD
    return dict(app = app,db = db,Rider = Rider,Role = Role)
=======
    return dict(app = app,db = db,User = User,Role = Role,Book = Book)
>>>>>>> dev

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()