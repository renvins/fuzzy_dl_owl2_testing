from pyowl2 import OWLOntology, OWLAnnotationProperty, IRI, OWLFullClass, OWLFullIndividual, \
    OWLDeclaration, OWLAnnotation, OWLLiteral, OWLClassAssertion
from rdflib import URIRef, Namespace, Literal, XSD
from tests.conftest import run_conversion_and_validation

def create_degree_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_degree#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    high_person = OWLFullClass(IRI(namespace, "HighPerson"))
    low_person = OWLFullClass(IRI(namespace, "LowPerson"))

    marco = OWLFullIndividual(IRI(namespace, "Marco"))
    vincenzo = OWLFullIndividual(IRI(namespace, "Vincenzo"))

    xml_string = "<fuzzyOwl2 fuzzyType=\"axiom\"><Degree value=\"0.6\"></Degree></fuzzyOwl2>"
    xml_literal = OWLLiteral(Literal(xml_string, datatype=XSD.string))

    marco_is_high = OWLAnnotation(fuzzy_label, xml_literal)

    marco.add_assertion(high_person.class_, annotations=[marco_is_high])
    vincenzo.add_assertion(low_person.class_)

    ontology.add_axioms([high_person, low_person, marco, vincenzo, OWLDeclaration(fuzzy_label)])
    ontology.save(str(owl_path))

def test_degree(test_setup_factory):
    print("\n--- Starting Degree Test ---")
    converter, original_path, final_path = test_setup_factory("test_degree", create_degree_ontology)

    run_conversion_and_validation(converter, original_path, final_path)