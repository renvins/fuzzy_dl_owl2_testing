from pyowl2 import OWLOntology, OWLFullClass, OWLFullIndividual, IRI, OWLAnnotationProperty, OWLDeclaration
from rdflib import URIRef, Namespace

from tests.conftest import test_setup_factory, run_conversion_and_validation

def create_assertion_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_assertion#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)

    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))
    fuzzy_label_declared = OWLDeclaration(fuzzy_label)

    person = OWLFullClass(IRI(namespace, "Person"))
    individual = OWLFullIndividual(IRI(namespace, "Vincenzo"))

    individual.add_assertion(person.class_)

    ontology.add_axioms([person, individual, fuzzy_label_declared])
    ontology.save(str(owl_path))

def test_assertion(test_setup_factory):
    print("\n--- Starting Assertion Test ---")
    converter, original_path, final_path = test_setup_factory("test_assertion", create_assertion_ontology)

    run_conversion_and_validation(converter, original_path, final_path)