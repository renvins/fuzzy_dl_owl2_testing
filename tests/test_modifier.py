from pyowl2 import OWLOntology, OWLFullClass, IRI, OWLAnnotationProperty, OWLDatatype, OWLAnnotationAssertion, \
    OWLLiteral, OWLDeclaration
from rdflib import URIRef, Namespace, Literal, XSD

from tests.conftest import run_conversion_and_validation

def create_modifier_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_modifier#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    high_person = OWLFullClass(IRI(namespace, "HighPerson"))
    very_high_person = OWLFullClass(IRI(namespace, "VeryHighPerson"))

    very_fuzzy = OWLDatatype(IRI(namespace, "very"))
    very_fuzzy_xml = "<fuzzyOwl2 fuzzyType=\"modifier\"><Modifier type=\"linear\" c=\"0.8\"></Modifier></fuzzyOwl2>"
    very_fuzzy_annotation = OWLAnnotationAssertion(very_fuzzy.iri, fuzzy_label, OWLLiteral(Literal(very_fuzzy_xml, datatype=XSD.string)))

    very_high_person_xml = "<fuzzyOwl2 fuzzyType=\"concept\"><Concept type=\"modified\" modifier=\"very\" base=\"HighPerson\"></Concept></fuzzyOwl2>"
    very_high_person_annotation = OWLAnnotationAssertion(very_high_person.class_.iri, fuzzy_label,
                                                         OWLLiteral(Literal(very_high_person_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(very_fuzzy), high_person, very_high_person,
                         very_fuzzy_annotation, very_high_person_annotation])
    ontology.save(str(owl_path))

def test_modifier(test_setup_factory):
    print("\n--- Starting Modifier Test ---")
    converter, original_path, final_path = test_setup_factory("test_modifier", create_modifier_ontology)

    run_conversion_and_validation(converter, original_path, final_path)