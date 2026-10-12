"""Happy-path test with a pure-Python fake descriptor. Touches no hardware."""

FAKE_PROFILE = {"idVendor": 0x2C97, "interfaces": [{"class": 0x03}]}


def fake_device():
    return {"idVendor": 0x2C97, "interfaces": [{"class": 0x03}]}


def matches(device, profile):
    return device == profile


def test_emulated_device_matches_profile():
    assert matches(fake_device(), FAKE_PROFILE)


def test_extra_interface_does_not_match():
    dev = fake_device()
    dev["interfaces"].append({"class": 0x08})
    assert not matches(dev, FAKE_PROFILE)
