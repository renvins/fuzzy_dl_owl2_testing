from pyowl2 import OWLOntology, OWLAnnotationProperty, IRI, OWLAnnotationAssertion, OWLFullClass, OWLFullIndividual, \
    OWLDeclaration, OWLFullDataRange, OWLDatatype, OWLAnnotation, OWLLiteral, OWLClassAssertion
from rdflib import URIRef, Namespace, Literal, XSD, RDF
from pathlib import Path
from conversion.validator import Validator

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

    annotation = OWLAnnotation(fuzzy_label, xml_literal)

    class_assertion_axiom = OWLClassAssertion(high_person.class_, marco.individual, annotations=[annotation])

    ontology.add_axioms([high_person, low_person, marco, vincenzo, OWLDeclaration(fuzzy_label), OWLClassAssertion(low_person.class_, vincenzo.individual), class_assertion_axiom])
    ontology.save(str(owl_path))

def test_degree(test_setup_factory):
    print("\n--- Starting Degree Test ---")
    converter, original_path, final_path = test_setup_factory("test_degree", create_degree_ontology)

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