"""Tests for the Technical challenge for selective process."""

import pytest

from source.customer_success_balancing import customer_success_balancing


# Start of company written tests ##############################################
def build_size_entities(size: int, score: int) -> list[dict[str, int]]:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    return [{"id": index + 1, "score": score} for index in range(size)]


def map_entities(array: list[int]) -> list[dict[str, int]]:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    return [
        {"id": index + 1, "score": item} for index, item in enumerate(array)
    ]


def array_sequence(count: int, start_at: int) -> list[int]:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    return [index + start_at for index in range(count)]


def test_scenario_1() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = [
        {"id": 1, "score": 60},
        {"id": 2, "score": 20},
        {"id": 3, "score": 95},
        {"id": 4, "score": 75},
    ]
    customers = [
        {"id": 1, "score": 90},
        {"id": 2, "score": 20},
        {"id": 3, "score": 70},
        {"id": 4, "score": 40},
        {"id": 5, "score": 60},
        {"id": 6, "score": 10},
    ]
    cs_away = [2, 4]

    assert customer_success_balancing(css, customers, cs_away) == 1


def test_scenario_2() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities([11, 21, 31, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away: list[int] = []

    assert customer_success_balancing(css, customers, cs_away) == 0


@pytest.mark.timeout(0.1)
def test_scenario_3() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities(array_sequence(999, 1))
    customers = build_size_entities(10000, 998)
    cs_away = [999]

    assert customer_success_balancing(css, customers, cs_away) == 998


def test_scenario_4() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities([1, 2, 3, 4, 5, 6])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away: list[int] = []

    assert customer_success_balancing(css, customers, cs_away) == 0


def test_scenario_5() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities([100, 2, 3, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away: list[int] = []

    assert customer_success_balancing(css, customers, cs_away) == 1


def test_scenario_6() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities([100, 99, 88, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = [1, 3, 2]

    assert customer_success_balancing(css, customers, cs_away) == 0


def test_scenario_7() -> None:
    # pylint: disable=missing-function-docstring
    # noqa: D103
    css = map_entities([100, 99, 88, 3, 4, 5])
    customers = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
    cs_away = [4, 5, 6]

    assert customer_success_balancing(css, customers, cs_away) == 3


# End of company written tests ################################################
