import pytest
from pathlib import Path

from converter import Converter
from validator import Validator

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

def run_conversion_and_validation(converter, original_path, final_path):
    converter.translate_owl2_to_fdl()
    assert converter.fdl_file.exists(), "FDL file was not created."

    converter.translate_fdl_to_owl2(final_path)
    assert Path(final_path).exists(), "Final OWL file was not created."

    print("Final file created. Now validating...")
    validator = Validator(original_path, final_path)

    validator.compare_classes()
    validator.compare_individuals()
    validator.compare_properties()
    validator.compare_axioms()

    print("✅ All assertions passed successfully.")