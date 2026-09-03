def test_get_activities_returns_all_activity_details(client):
    # Arrange
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Tennis Team",
        "Basketball Club",
        "Art Studio",
        "Music Band",
        "Math Club",
        "Debate Team",
    }
    expected_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities_response = response.json()
    assert set(activities_response) == expected_activity_names
    for activity in activities_response.values():
        assert set(activity) == expected_fields
        assert isinstance(activity["participants"], list)
