from os import name
from rdflib import Literal, Namespace, XSD, URIRef

from pyowl2 import OWLAnnotationProperty, OWLDatatype, OWLDatatypeRestriction, OWLDatatypeDefinition, OWLAnnotationAssertion, OWLDeclaration, OWLFacet, OWLLiteral, OWLOntology, IRI
from conftest import run_conversion_and_validation


def create_r_shoulder_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_r_shoulder#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    XSD_namespace = Namespace(str(XSD))
    integer_datatype = OWLDatatype(IRI(XSD_namespace, "integer"))

    high_price = OWLDatatype(IRI(namespace, "HighPrice"))
    high_price_xml = "<fuzzyOwl2 fuzzyType=\"datatype\"><Datatype type=\"rightshoulder\" a=\"800\" b=\"1500\"></Datatype></fuzzyOwl2>"
    high_price_assertion = OWLAnnotationAssertion(high_price.iri, fuzzy_label, OWLLiteral(Literal(high_price_xml, datatype=XSD.string)))

    min_price = OWLFacet(XSD.minInclusive, OWLLiteral(Literal("0", datatype=XSD.integer)))
    max_price = OWLFacet(XSD.maxInclusive, OWLLiteral(Literal("2000", datatype=XSD.integer)))

    high_price_restriction = OWLDatatypeRestriction(integer_datatype, restrictions=[min_price, max_price])
    high_price_definition = OWLDatatypeDefinition(high_price, high_price_restriction)

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(high_price), high_price_definition, high_price_assertion])
    ontology.save(str(owl_path))

def test_r_shoulder(test_setup_factory):
    print("\n--- Starting R Shoulder Test ---")
    converter, original_path, final_path = test_setup_factory("test_r_shoulder", create_r_shoulder_ontology)

    run_conversion_and_validation(converter, original_path, final_path)