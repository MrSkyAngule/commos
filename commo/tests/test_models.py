import pytest
from commo.models import Commo


@pytest.mark.django_db
def test_commo_model():
    item = Commo.objects.create(
        device_id='nimu',
        data='datas'
    )
    assert item.device_id == 'nimu'
    assert item.data == 'datas'
    assert Commo.objects.count() == 1
