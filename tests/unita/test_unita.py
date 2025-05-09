import re

import pint
import pint.testing
import pytest

from unit_test_prj.coscente_unita import somma_unit_aware

Q = pint.get_application_registry().Quantity


def test_add_unit_aware():
    a = Q(1.0, "m")
    b = Q(1.0, "cm")

    comp = Q(1.01, "m")

    res = somma_unit_aware(a, b)

    pint.testing.assert_equal(res, comp)


def test_errore():
    a = Q(1.0, "m")
    b = Q(1.0, "kg")

    with pytest.raises(
        TypeError,
        match=re.escape(
            "Cannot convert from 'meter' ([length]) to 'kilogram' ([mass])"
        ),
    ):
        somma_unit_aware(a, b)
