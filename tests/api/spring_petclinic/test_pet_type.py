import requests

from tests.core.test_base import TestBase


class TestPetTypeAPI(TestBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.http_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def test_pettype_crud_operations(self):
        self.logger.info('Starting test_pettype_crud_operations')

        # Create PetType
        unique_id = self.get_prop('unique_id')
        pettype_name = f"cat-{unique_id}"
        pettype_base_url = f"{self.get_prop("spring_petclinic_restservice_url")}/pettypes"
        http_payload = {
            "name": pettype_name
        }

        response = requests.post(pettype_base_url, json=http_payload, headers=self.http_headers)

        assert response.status_code == 201
        response_data = response.json()
        pettype_id = response_data["id"]
        self.logger.info(f"Created - Pet Type Name: {pettype_name} , Response: {response_data}")

        # Read PetType
        http_session = requests.Session()
        http_session.headers.update(self.http_headers)
        pettype_rud_url = f"{pettype_base_url}/{pettype_id}"

        response = http_session.get(pettype_rud_url)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["name"] == pettype_name

        # Update PetType Name
        updated_pettype_name = f"{pettype_name}-updated-{pettype_id}"
        http_payload = {
            "id": pettype_id,
            "name": updated_pettype_name
        }

        self.logger.info(f"Pet Type ID: {pettype_id} , Updated Pet Type Name: {updated_pettype_name} , URL: {pettype_rud_url}")
        response = http_session.put(pettype_rud_url, json=http_payload, headers=self.http_headers)

        assert response.status_code == 204

        # Read again and check name has been updated
        response = http_session.get(pettype_rud_url)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["name"] == updated_pettype_name

        # Delete the Pet type
        response = http_session.delete(pettype_rud_url)
        assert response.status_code == 204

        # Read again - Verify operation fails
        response = http_session.get(pettype_rud_url)
        assert response.status_code == 404

        self.logger.info('Complete test_pettype_crud_operations')

    @classmethod
    def teardown_class(cls):
        super().teardown_class()