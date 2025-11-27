import pytest

from ..predicates.loader.pred_config import load_constructions_and_macros


@pytest.fixture(autouse=True)
def load_constructions_and_macros_for_tests():
    load_constructions_and_macros()
