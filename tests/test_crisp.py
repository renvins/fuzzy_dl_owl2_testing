from pyowl2 import OWLAnnotationAssertion, OWLAnnotationProperty, OWLDatatypeDefinition, OWLDatatypeRestriction, OWLDeclaration, OWLLiteral
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.ontology import OWLOntology
from pyowl2.utils.datatype import OWLFacet
from rdflib import XSD, Literal, Namespace, URIRef

from conftest import run_conversion_and_validation

def create_crisp_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_crisp#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    medium_temp_dt = OWLDatatype(IRI(namespace, "MediumTemp"))

    xsd_namespace = Namespace(str(XSD))
    integer_datatype = OWLDatatype(IRI(xsd_namespace, "integer"))

    min_temp = OWLFacet(XSD.minInclusive, OWLLiteral(Literal("0", datatype=XSD.integer)))
    max_temp = OWLFacet(XSD.maxInclusive, OWLLiteral(Literal("100", datatype=XSD.integer)))

    medium_temp_restr = OWLDatatypeRestriction(integer_datatype, [min_temp, max_temp])
    medium_temp_def = OWLDatatypeDefinition(medium_temp_dt, medium_temp_restr)

    medium_temp_xml = """
    <fuzzyOwl2 fuzzyType="datatype">
        <Datatype type="crisp" a="20.0" b="30.0"></Datatype>
    </fuzzyOwl2>
    """
    medium_temp_ass = OWLAnnotationAssertion(medium_temp_dt, fuzzy_label, OWLLiteral(Literal(medium_temp_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label),OWLDeclaration(medium_temp_dt), medium_temp_def, medium_temp_ass])
    ontology.save(str(owl_path))

def test_crisp(test_setup_factory):
    print("\n--- Starting Crisp Test ---")
    converter, original_path, final_path = test_setup_factory("test_crisp", create_crisp_ontology)

    run_conversion_and_validation(converter, original_path, final_path)
