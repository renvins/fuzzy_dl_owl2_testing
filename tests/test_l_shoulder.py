from pyowl2 import OWLAnnotationAssertion, OWLDeclaration, OWLFacet, OWLLiteral, OWLOntology, OWLAnnotationProperty, OWLDatatype, IRI, OWLDatatypeRestriction, OWLDatatypeDefinition
from rdflib import Literal, Namespace, XSD, URIRef

from conftest import run_conversion_and_validation


def create_l_shoulder_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_l_shoulder#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    XSD_namespace = Namespace(str(XSD))
    integer_datatype = OWLDatatype(IRI(XSD_namespace, "integer"))

    young_datatype = OWLDatatype(IRI(namespace, "YoungAge"))

    min_age = OWLFacet(XSD.minInclusive, OWLLiteral(Literal("0", datatype=XSD.integer)))
    max_age = OWLFacet(XSD.maxInclusive, OWLLiteral(Literal("100", datatype=XSD.integer)))

    young_restriction = OWLDatatypeRestriction(integer_datatype, restrictions=[min_age, max_age])

    young_definition = OWLDatatypeDefinition(young_datatype, young_restriction)
    young_age_xml = "<fuzzyOwl2 fuzzyType=\"datatype\"><Datatype type=\"leftshoulder\" a=\"20\" b=\"35\"></Datatype></fuzzyOwl2>"

    young_assertion = OWLAnnotationAssertion(young_datatype.iri, fuzzy_label, OWLLiteral(Literal(young_age_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(young_datatype), young_definition, young_assertion])
    ontology.save(str(owl_path))

def test_l_shoulder(test_setup_factory):
    print("\n--- Starting L Shoulder Test ---")
    converter, original_path, final_path = test_setup_factory("test_l_shoulder", create_l_shoulder_ontology)

    run_conversion_and_validation(converter, original_path, final_path)