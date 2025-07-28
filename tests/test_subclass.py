from pyowl2 import OWLOntology, OWLFullClass, IRI, OWLSubClassOf, OWLAnnotationProperty, OWLDeclaration
from rdflib import URIRef, Namespace

from tests.conftest import run_conversion_and_validation

def create_subclass_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_subclass#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)

    fuzzyLabel = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    person = OWLFullClass(IRI(namespace, "Person"))
    student = OWLFullClass(IRI(namespace, "Student"))

    subclass = OWLSubClassOf(student.class_, person.class_)
    ontology.add_axioms([OWLDeclaration(fuzzyLabel), person, student, subclass])

    ontology.save(str(owl_path))

def test_subclass(test_setup_factory):
    print("\n--- Starting Subclass Test ---")
    converter, original_path, final_path = test_setup_factory("test_subclass", create_subclass_ontology)
    run_conversion_and_validation(converter, original_path, final_path)