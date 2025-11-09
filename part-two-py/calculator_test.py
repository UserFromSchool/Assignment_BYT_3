import pytest
import re
from calculator import Calculator


########################## ADDITION TESTS ##########################
@pytest.mark.parametrize(
    ["left_operand", "right_operand", "expected"],
    [
        (1, 1, 2),
        (3, 5, 8),
        (12, 45, 57),
        (12.3, 45.6, 57.9),
        (-1, 1, 0),
        (1_000_000_000_000_000_000, 1_000_000_000_000_000_000, 2_000_000_000_000_000_000),
    ]
)
def test_addition_correct_examples(left_operand: float, right_operand: float, expected: float) -> None:
    assert Calculator("+").calculate(left_operand, right_operand) == pytest.approx(expected, abs=0.001)


@pytest.mark.parametrize(
    ["left_operand", "right_operand"],
    [
        ("1", 1),
        (3, None),
        ({ 14: 14 }, {}),
        ([], []),
        ("B", "A"),
    ]
)
def test_addition_incorrect_examples(left_operand: float, right_operand: float) -> None:
    with pytest.raises(TypeError):
        Calculator("+").calculate(left_operand, right_operand)


########################## SUBTRACTION TESTS ##########################
@pytest.mark.parametrize(
    ["left_operand", "right_operand", "expected"],
    [
        (1, 1, 0),
        (3, 5, -2),
        (12, 45, -33),
        (12.3, 45.6, -33.3),
        (-1, 1, -2),
        (100, 1, 99),
        (100, -1, 101),
        (1_000_000_000_000_000_000, 1_000_000_000_000_000_000, 0),
    ]
)
def test_subtraction_correct_examples(left_operand: float, right_operand: float, expected: float) -> None:
    assert Calculator("-").calculate(left_operand, right_operand) == pytest.approx(expected, abs=0.001)


@pytest.mark.parametrize(
    ["left_operand", "right_operand"],
    [
        ("1", 1),
        (3, None),
        ({ 14: 14 }, {}),
        ([], []),
        ("B", "A"),
    ]
)
def test_subtraction_incorrect_examples(left_operand: float, right_operand: float) -> None:
    with pytest.raises(TypeError):
        Calculator("-").calculate(left_operand, right_operand)


########################## MULTIPLICATION TESTS ##########################
@pytest.mark.parametrize(
    ["left_operand", "right_operand", "expected"],
    [
        (1, 1, 1),
        (3, 5, 15),
        (12, 45, 540),
        (12.3, 45.6, 560.88),
        (-1, 1, -1),
        (0.1, 0.1, 0.01),
        (1_000_000_000_000_000_000, 1_000_000_000_000_000_000, 1_000_000_000_000_000_000_000_000_000_000_000_000),
    ]
)
def test_multiplication_correct_examples(left_operand: float, right_operand: float, expected: float) -> None:
    assert Calculator("*").calculate(left_operand, right_operand) == pytest.approx(expected, abs=0.001)


@pytest.mark.parametrize(
    ["left_operand", "right_operand"],
    [
        ("1", 1),
        (3, None),
        ({ 14: 14 }, {}),
        ([], []),
        ("B", "A"),
    ]
)
def test_multiplication_incorrect_examples(left_operand: float, right_operand: float) -> None:
    with pytest.raises(TypeError):
        Calculator("*").calculate(left_operand, right_operand)


########################## DIVISION TESTS ##########################
@pytest.mark.parametrize(
    ["left_operand", "right_operand", "expected"],
    [
        (1, 1, 1),
        (-3, 2, -1.5),
        (-12, -4, 3),
        (-12.3, -4.6, 2.673913043478261),
        (0.1, 0.1, 1),
        (1_000_000_000_000_000_000, 1_000_000_000_000_000_000, 1),
    ]
)
def test_division_correct_examples(left_operand: float, right_operand: float, expected: float) -> None:
    assert Calculator("/").calculate(left_operand, right_operand) == pytest.approx(expected, abs=0.001)


@pytest.mark.parametrize(
    ["left_operand", "right_operand"],
    [
        ("1", 1),
        (3, None),
        ({ 14: 14 }, {}),
        ([], []),
        ("B", "A"),
    ]
)
def test_division_incorrect_examples(left_operand: float, right_operand: float) -> None:
    with pytest.raises(TypeError):
        Calculator("/").calculate(left_operand, right_operand)


def test_division_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        Calculator("/").calculate(1, 0)

    
########################## OTHER TESTS ##########################
@pytest.mark.parametrize(
    ["operation"],
    [
        ("^",),
        ("%",),
        ("#",),
        ("@",),
        ("!",),
        ("$",),
        ("&",),
        ("**",),
        ("add",),
        ("subtract",),
    ]
)
def test_invalid_operation(operation: str) -> None:
    with pytest.raises(
        NotImplementedError,
        match=re.escape(f"Operation not supported: {operation}")
    ):
        Calculator(operation)


def test_str_representation() -> None:
    assert str(Calculator("+")) == "Caclulator supporting + operation."
    assert str(Calculator("-")) == "Caclulator supporting - operation."
    assert str(Calculator("*")) == "Caclulator supporting * operation."
    assert str(Calculator("/")) == "Caclulator supporting / operation."


def test_repr_representation() -> None:
    assert repr(Calculator("+")) == "Calculator(mode=+)"
    assert repr(Calculator("-")) == "Calculator(mode=-)"
    assert repr(Calculator("*")) == "Calculator(mode=*)"
    assert repr(Calculator("/")) == "Calculator(mode=/)"