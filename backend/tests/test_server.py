import pytest
from pydantic import ValidationError

from app.models import LoadAverage, Server, ServerStatus


def test_server_json_round_trip():
    payload = {
        "name": "Lab server",
        "hostname": "lab.local",
        "status": "online",
        "cpu_usage": 25.5,
        "load": 2,
        "load_average": {"one_minute": 1.5, "five_minutes": 1.0, "fifteen_minutes": 0.75},
        "memory_usage": 60.0,
        "disk_usage": 40.0,
    }
    server = Server.model_validate(payload)
    assert server.status is ServerStatus.ONLINE
    assert server.model_dump(mode="json") == payload
    assert Server.model_validate_json(server.model_dump_json()) == server


def test_unknown_measurements_are_not_zero():
    server = Server(name=" Lab ", hostname=" lab.local ")
    assert server.name == "Lab"
    assert server.hostname == "lab.local"
    assert server.status is ServerStatus.UNKNOWN
    for field in ("cpu_usage", "load", "load_average", "memory_usage", "disk_usage"):
        assert server.model_dump()[field] is None


@pytest.mark.parametrize("status", ["online", "offline", "unknown"])
def test_status_values(status):
    assert Server(name="Lab", hostname="lab.local", status=status).status.value == status


@pytest.mark.parametrize("field", ["cpu_usage", "memory_usage", "disk_usage"])
@pytest.mark.parametrize("value", [-1, 100.1, float("nan"), float("inf")])
def test_invalid_usage_is_rejected(field, value):
    with pytest.raises(ValidationError):
        Server(name="Lab", hostname="lab.local", **{field: value})


@pytest.mark.parametrize("value", [0, 100])
def test_usage_boundaries(value):
    server = Server(name="Lab", hostname="lab.local", cpu_usage=value,
                    memory_usage=value, disk_usage=value)
    assert server.cpu_usage == server.memory_usage == server.disk_usage == value


@pytest.mark.parametrize("field", ["name", "hostname"])
@pytest.mark.parametrize("value", ["", "   "])
def test_blank_identifiers_are_rejected(field, value):
    payload = {"name": "Lab", "hostname": "lab.local", field: value}
    with pytest.raises(ValidationError):
        Server.model_validate(payload)


@pytest.mark.parametrize("field", ["name", "hostname"])
def test_identifiers_are_required(field):
    payload = {"name": "Lab", "hostname": "lab.local"}
    del payload[field]
    with pytest.raises(ValidationError):
        Server.model_validate(payload)


def test_invalid_status_is_rejected():
    with pytest.raises(ValidationError):
        Server(name="Lab", hostname="lab.local", status="broken")


@pytest.mark.parametrize("value", [-1, 1.5, True])
def test_load_requires_nonnegative_task_count(value):
    with pytest.raises(ValidationError):
        Server(name="Lab", hostname="lab.local", load=value)


@pytest.mark.parametrize("field", ["one_minute", "five_minutes", "fifteen_minutes"])
@pytest.mark.parametrize("value", [-0.1, float("nan"), float("inf")])
def test_invalid_load_average_is_rejected(field, value):
    payload = {"one_minute": 0, "five_minutes": 0, "fifteen_minutes": 0, field: value}
    with pytest.raises(ValidationError):
        LoadAverage.model_validate(payload)


def test_load_averages_can_exceed_one_hundred():
    average = LoadAverage(one_minute=120, five_minutes=110, fifteen_minutes=101)
    assert average.one_minute == 120
