import pytest


def test_orm_available_models_exists():
    """OzonOrm espone orm_available_models come dict vuoto all'avvio."""
    from ozonenv.core.OzonOrm import OzonOrm

    class FakeEnv:
        lang = "it"
        db = None
        config_system = {"models_folder": "/models"}
        app_code = "test"
        cls_model = object
        models_folder = "/models"

    orm = OzonOrm(FakeEnv())
    assert hasattr(orm, "orm_available_models")
    assert isinstance(orm.orm_available_models, dict)
    assert len(orm.orm_available_models) == 0


@pytest.mark.asyncio
async def test_load_model_returns_none_for_unknown():
    """_load_model restituisce None per modelli non in orm_available_models."""
    from ozonenv.core.OzonOrm import OzonOrm

    class FakeEnv:
        lang = "it"
        db = None
        config_system = {"models_folder": "/models"}
        app_code = "test"
        cls_model = object
        models_folder = "/models"
        models = {}

    orm = OzonOrm(FakeEnv())
    result = await orm._load_model("nonexistent_model")
    assert result is None
