from pyowl2 import OWLDatatype, OWLDatatypeDefinition, OWLDatatypeRestriction, OWLFacet, OWLFullClass, OWLOntology, OWLAnnotationProperty, OWLDeclaration, IRI, OWLAnnotationAssertion, OWLLiteral
from rdflib import Namespace, URIRef, Literal, XSD

from conftest import run_conversion_and_validation

def create_qowa_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_qowa#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    most_quantifier = OWLDatatype(IRI(namespace, "MostQuantifier"))

    xsd_namespace = Namespace(str(XSD))
    integer_datatype = OWLDatatype(IRI(xsd_namespace, "integer"))

    min_value = OWLFacet(XSD.minInclusive, OWLLiteral(Literal("0", datatype=XSD.integer)))
    max_value = OWLFacet(XSD.maxInclusive, OWLLiteral(Literal("50", datatype=XSD.integer)))

    datatype_restriction = OWLDatatypeRestriction(datatype=integer_datatype, restrictions=[min_value, max_value])
    datatype_definition = OWLDatatypeDefinition(most_quantifier, datatype_restriction)

    most_quantifier_xml = "<fuzzyOwl2 fuzzyType=\"datatype\"><Datatype type=\"leftshoulder\" a=\"20\" b=\"35\"></Datatype></fuzzyOwl2>"

    most_quantifier_annotation = OWLAnnotationAssertion(most_quantifier.iri, fuzzy_label, OWLLiteral(Literal(most_quantifier_xml, datatype=XSD.string)))

    excellent_hotel = OWLFullClass(IRI(namespace, "ExcellentHotel"))
    excellent_xml = """
    <fuzzyOwl2 fuzzyType="concept">
            <Concept type="qowa" quantifier="MostQuantifier">
                <Names>
                    <Name>Cheap</Name>
                    <Name>CloseToVenue</Name>
                    <Name>Comfortable</Name>
                    <Name>GoodService</Name>
                </Names>
            </Concept>
        </fuzzyOwl2>
    """
    excellent_assertion = OWLAnnotationAssertion(excellent_hotel.class_.iri, fuzzy_label, OWLLiteral(Literal(excellent_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(most_quantifier), datatype_definition, most_quantifier_annotation, excellent_hotel, excellent_assertion])
    ontology.save(str(owl_path))

def test_qowa(test_setup_factory):
    print("\n--- Starting QOWA Test ---")
    converter, original_path, final_path = test_setup_factory("test_qowa", create_qowa_ontology)

    run_conversion_and_validation(converter, original_path, final_path)