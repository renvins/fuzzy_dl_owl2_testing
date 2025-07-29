from pyowl2 import OWLOntology, OWLAnnotationProperty, IRI, OWLFullClass, OWLAnnotationAssertion, OWLLiteral, \
    OWLDeclaration
from rdflib import URIRef, Namespace, Literal, XSD

from tests.conftest import run_conversion_and_validation

def create_weighted_sum_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_modifier#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    reduced_consumption = OWLFullClass(IRI(namespace, "ReducedConsumption"))
    low_price = OWLFullClass(IRI(namespace, "LowPrice"))
    internal_space = OWLFullClass(IRI(namespace, "InternalSpace"))

    customer_preferences = OWLFullClass(IRI(namespace, "CustomerPreferences"))

    weighted_sum_xml = """<fuzzyOwl2 fuzzyType=\"concept\">
                            <Concept type=\"weightedSum\">
                                <Concept type=\"weighted\" value=\"0.5\" base=\"LowPrice\"></Concept>
                                <Concept type=\"weighted\" value=\"0.3\" base=\"ReducedConsumption\"></Concept>
                                <Concept type="weighted" value="0.2" base="InternalSpace"></Concept>
                            </Concept>
                          </fuzzyOwl2>"""
    weighted_sum_annotation = OWLAnnotationAssertion(customer_preferences.class_.iri, fuzzy_label, OWLLiteral(Literal(weighted_sum_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), reduced_consumption, low_price, internal_space, customer_preferences, weighted_sum_annotation])
    ontology.save(str(owl_path))

def test_weighted_sum(test_setup_factory):
    print("\n--- Starting Weighted Sum Test ---")
    converter, original_path, final_path = test_setup_factory("test_weighted_sum", create_weighted_sum_ontology)

    run_conversion_and_validation(converter, original_path, final_path)
