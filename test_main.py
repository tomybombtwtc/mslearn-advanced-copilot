from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]
    def test_get_cities_spain() -> None:
        """
        Test the /countries/Spain/cities endpoint.

        This test checks that the endpoint returns the correct list of cities for Spain.
        It also verifies the response status code and data type.

        Edge Cases:
        - Ensures only cities present in the dataset are returned.
        """
        response = client.get("/countries/Spain/cities")
        assert response.status_code == 200
        cities = response.json()
        assert isinstance(cities, list)
        # Only Seville is present for Spain in the dataset
        expected_cities = ["Seville"]
        assert sorted(cities) == sorted(expected_cities)

    def test_get_cities_invalid_country() -> None:
        """
        Test the /countries/Atlantis/cities endpoint for a non-existent country.

        This test checks that the endpoint returns an empty list for an invalid country.
        """
        response = client.get("/countries/Atlantis/cities")
        assert response.status_code == 200
        cities = response.json()
        assert isinstance(cities, list)
        assert cities == []