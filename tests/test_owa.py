from pyowl2 import OWLAnnotationAssertion, OWLAnnotationProperty, OWLFullClass, OWLLiteral, OWLOntology, OWLDeclaration, IRI
from rdflib import Literal, Namespace, URIRef, XSD

from conftest import run_conversion_and_validation


def create_owa_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_owa#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    good_hotel = OWLFullClass(IRI(namespace, "GoodHotel"))

    good_hotel_xml = """
    <fuzzyOwl2 fuzzyType=\"concept\"><Concept type=\"owa\">
        <Weights>
            <Weight>0.6</Weight>
            <Weight>0.3</Weight>
            <Weight>0.1</Weight>
        </Weights>
        <Names>
            <Name>Cheap</Name>
            <Name>CloseToVenue</Name>
            <Name>Comfortable</Name>
        </Names>
    </Concept></fuzzyOwl2>
    """
    good_hotel_assertion = OWLAnnotationAssertion(good_hotel.class_.iri, fuzzy_label, OWLLiteral(Literal(good_hotel_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), good_hotel, good_hotel_assertion])
    ontology.save(str(owl_path))

def test_owa(test_setup_factory):
    print("\n--- Starting OWATest ---")
    converter, original_path, final_path = test_setup_factory("test_owa", create_owa_ontology)

    run_conversion_and_validation(converter, original_path, final_path)