import pytest
from controller.main_controller import *


def test_load_module():
	assert load_module(0) is None
	for index in range(4, 12):
		with pytest.raises(KeyError):
			load_module(index)
