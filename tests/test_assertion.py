import pytest
from pathlib import Path

from pyowl2 import OWLOntology, OWLFullClass, OWLFullIndividual, IRI
from rdflib import URIRef, Namespace

from conversion.validator import Validator
from tests.conftest import test_setup_factory

def create_assertion_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_assertion#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference)

    person = OWLFullClass(IRI(namespace, "Person"))
    individual = OWLFullIndividual(IRI(namespace, "Vincenzo"))

    individual.add_assertion(person.class_)

    ontology.add_axioms([person, individual])
    ontology.save(str(owl_path))

def test_assertion(test_setup_factory):
    print("\n--- Starting Assertion Test ---")
    converter, original_path, final_path = test_setup_factory("test_assertion", create_assertion_ontology)

    converter.translate_owl2_to_fdl()
    assert converter.fdl_file.exists(), "FDL file was not created."

    converter.translate_fdl_to_owl2(final_path)
    assert Path(final_path).exists(), "Final OWL file was not created."

    # Step 3: Create the Validator with the correct paths
    print("Final file created. Now validating...")
    validator = Validator(original_path, final_path)

    # Step 4: Run all your checks
    validator.compare_classes()
    validator.compare_individuals()
    validator.compare_properties()
    validator.compare_axioms()

    print("✅ All assertions passed successfully.")