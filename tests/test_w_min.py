from pyowl2 import IRI, OWLAnnotationAssertion, OWLAnnotationProperty, OWLDeclaration, OWLFullClass, OWLLiteral, OWLOntology
from rdflib import XSD, Literal, Namespace, URIRef

from conftest import run_conversion_and_validation

def create_w_min_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_w_min#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    a_class = OWLFullClass(IRI(namespace, "A"))
    b_class = OWLFullClass(IRI(namespace, "B"))

    w_min_class = OWLFullClass(IRI(namespace, "WMinAB"))
    w_min_xml = """
    <fuzzyOwl2 fuzzyType="concept">
        <Concept type="weightedMinimum">
            <Concept type="weighted" value="0.5" base="A"></Concept>
            <Concept type="weighted" value="1" base="B"></Concept>
        </Concept>
    </fuzzyOwl2>
    """
    w_min_ass = OWLAnnotationAssertion(w_min_class.class_.iri, fuzzy_label, OWLLiteral(Literal(w_min_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), a_class, b_class, w_min_class, w_min_ass])
    ontology.save(str(owl_path))

def test_w_min(test_setup_factory):
    print("\n--- Starting W Min Test ---")
    converter, original_path, final_path = test_setup_factory("test_w_min", create_w_min_ontology)

    run_conversion_and_validation(converter, original_path, final_path)