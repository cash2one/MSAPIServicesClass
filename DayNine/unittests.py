# from flask import json
import server
import unittest


class FlaskServerTest(unittest.TestCase):
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        assert response.status_code == 200, "status code was not okay"
        assert response.data == "Hello World!"

    def test_put_pet_existing_name(self):
        server.petShop += {"name": "john", "age": 10, "species": "dog"}
        response = self.app.put('/pets/john')
        assert response.status_code == 200, "status code was not okay"
        assert response.data == ""

    def test_put_pet_nonexisting_name(self):
        return

    def test_post_pet_existing_pet(self):
        return

    def test_post_pet_nonexisting_pet(self):
        return

    def test_get_pets(self):
        server.petShop += {"age": 10, "species": "dog", "name": "john"}
        server.petShop += {"age": 20, "species": "cat", "name": "george"}
        response = self.app.get('/pets')
        assert response.status_code == 200, "status code was not okay"
        assert response.data == '[{"age": "10", "name": "john",'
        '"species": "dog"}, {"age": "20", "name": "george", '
        '"species": "cat"}]'

    def test_get_existing_pet(self):
        return

    def test_get_nonexisting_pet(self):
        return

    def test_delete_pet_with_existing_name(self):
        return

    def test_delete_pet_with_nonexisting_name(self):
        return

if __name__ == '__main__':
    unittest.main()
