from pyowl2 import OWLAnnotationAssertion, OWLAnnotationProperty, OWLDatatype, OWLFullClass, OWLOntology, OWLLiteral, OWLDeclaration, IRI
from rdflib import Literal, Namespace, URIRef, XSD

from conftest import run_conversion_and_validation

def create_triangular_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_triangular#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    ripe = OWLFullClass(IRI(namespace, "Ripe"))
    very_ripe = OWLFullClass(IRI(namespace, "VeryRipe"))
    very_ripe.is_subclass_of(ripe)

    very_datatype = OWLDatatype(IRI(namespace, "very"))
    very_datatype_xml = "<fuzzyOwl2 fuzzyType=\"modifier\"><Modifier type=\"triangular\" a=\"0.5\" b=\"1.0\" c=\"1.0\"></Modifier></fuzzyOwl2>"
    very_datatype_annotation = OWLAnnotationAssertion(very_datatype.iri, fuzzy_label, OWLLiteral(Literal(very_datatype_xml, datatype=XSD.string)))

    very_ripe_xml = "<fuzzyOwl2 fuzzyType=\"concept\"><Concept type=\"modified\" modifier=\"very\" base=\"Ripe\"></Concept></fuzzyOwl2>"
    very_ripe_annotation = OWLAnnotationAssertion(very_ripe.class_.iri, fuzzy_label, OWLLiteral(Literal(very_ripe_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(very_datatype), ripe, very_ripe,
                         very_datatype_annotation, very_ripe_annotation])
    ontology.save(str(owl_path))

def test_triangular(test_setup_factory):
    print("\n--- Starting Triangular Test ---")
    converter, original_path, final_path = test_setup_factory("test_triangular", create_triangular_ontology)

    run_conversion_and_validation(converter, original_path, final_path)