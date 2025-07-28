from pyowl2 import OWLOntology, OWLAnnotationProperty, IRI, OWLFullClass, OWLDisjointClasses, OWLDeclaration
from rdflib import URIRef, Namespace

from tests.conftest import run_conversion_and_validation

def create_disjoint_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_disjoint#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)

    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    person = OWLFullClass(IRI(namespace, "Person"))
    animal = OWLFullClass(IRI(namespace, "Animal"))

    disjoint_classes = OWLDisjointClasses([person.class_, animal.class_])

    ontology.add_axioms([OWLDeclaration(fuzzy_label), person, animal, disjoint_classes])
    ontology.save(str(owl_path))

def test_disjoint(test_setup_factory):
    print("\n--- Starting Disjoint Test ---")
    converter, original_path, final_path = test_setup_factory("test_disjoint", create_disjoint_ontology)

    run_conversion_and_validation(converter, original_path, final_path)