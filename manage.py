from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from database import Base


manager = Manager(app)
migrate = Migrate(app, Base)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()