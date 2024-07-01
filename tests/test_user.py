import unittest
from models.user import User
from models import storage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestUserModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('mysql+mysqldb://hbnb_test:hbnb_test_pwd@localhost/hbnb_test_db')
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.engine.dispose()

    def setUp(self):
        self.user = User(email="test@example.com",password='password', first_name="john", last_name="doe")
        self.session.add(self.user)
        self.session.commit()

    def tearDown(self):
        self.session.query(User).delete()
        self.session.commit()

    def test_user_creation(self):
        user = self.session.query(User).filter_by(email="test@example.com").first()
        self.assertIsNotNone(user)
        self.assertEqual(User.email,"test@example.com")
        self.assertEqual(user.first_name, "john")
        self.assertEqual(user.last_name, "doe")

if __name__ == '__main__':
    unittest.main()
