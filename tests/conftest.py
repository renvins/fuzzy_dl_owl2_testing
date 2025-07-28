import pytest
from pathlib import Path

from conversion.converter import Converter

OUTPUT_DIR = Path("test_outputs")

@pytest.fixture
def test_setup_factory():
    def _setup_test(test_name: str, create_ontology_func: callable):
        test_dir = OUTPUT_DIR / test_name
        test_dir.mkdir(parents=True, exist_ok=True)

        original_owl_path = (test_dir / f"{test_name}.owl").resolve()
        fdl_path = (test_dir / f"{test_name}.fdl").resolve()
        final_owl_path = (test_dir / f"{test_name}_final.owl").resolve()

        create_ontology_func(original_owl_path)

        converter = Converter(original_owl_path, fdl_path)

        return converter, original_owl_path, final_owl_path
    yield _setup_test