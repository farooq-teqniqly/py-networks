import pytest
from teqniqly_networks.networks import Node


@pytest.mark.parametrize("key", [None, "", "  "])
def test_when_key_not_specified_raises_exception(key):
    with pytest.raises(ValueError) as error:
        Node(key, None)

    assert str(error.value) == "The 'key' parameter must be a non-empty string."
