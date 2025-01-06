USER = {
    "email": "fabian@prueba.com",
    "username": "fabianusername",
    "password": "fabianpassword",
    "address": "fabian address"
}

class TestUserAPI:


    def test_create_user(self, test_client):
        response = test_client.post("/users/", json=USER)
        assert response.status_code == 201, f"Error: {response.json()}"
        assert response.json()['username'] == USER['username']


    def test_duplicated_user(self, test_client):
        test_client.post("/users/", json=USER)
        create_response = test_client.post("/users/", json=USER)
        assert create_response.status_code == 409, f"Error: {create_response.json()}"


    def test_get_users(self, auth_token, test_client):
        get_users_response = test_client.get("/users/", headers={"Authorization": f"Bearer {auth_token}"})
        assert get_users_response.status_code == 200, f"Error: {get_users_response.json()}"
        assert isinstance(get_users_response.json()['data'], list)


    def test_get_user_by_id(self, test_client):
        new_user = test_client.post("/users/", json=USER)
        user_id = new_user.json()['id']
        res = test_client.post("/auth/login", data={"username": USER['username'], "password": USER['password']})
        jwt = res.json()['access_token']
        response = test_client.get(f"/users/{user_id}", headers={"Authorization": f"Bearer {jwt}"})
        response.json()
        assert response.status_code == 200, f"Error: {response.json()}"
        assert response.json()['id'] == user_id


    def test_delete_user(self, test_client):
        new_user = test_client.post("/users/", json=USER)
        user_id = new_user.json()['id']
        res = test_client.post("/auth/login", data={"username": USER['username'], "password": USER['password']})
        jwt = res.json()['access_token']
        response = test_client.delete(f"/users/{user_id}", headers={"Authorization": f"Bearer {jwt}"})
        assert response.status_code == 204, f"Error: {response.json()}"
        assert response.text == ""


    def test_update_user(self, test_client):
        new_user = test_client.post("/users/", json=USER)
        user_id = new_user.json()['id']
        res = test_client.post("/auth/login", data={"username": USER['username'], "password": USER['password']})
        jwt = res.json()['access_token']
        response = test_client.put(f"/users/{user_id}", json={"username": "asd"}, headers={"Authorization": f"Bearer {jwt}"})
        assert response.status_code == 200, f"Error: {response.json()}"
        response = test_client.get(f"/users/{user_id}", headers={"Authorization": f"Bearer {jwt}"})
        assert response.json()['username'] == "asd"
        assert response.json()['address'] == "fabian address"
