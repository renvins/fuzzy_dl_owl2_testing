from pyowl2 import IRI, OWLAnnotationAssertion, OWLAnnotationProperty, OWLClass, OWLClassAssertion, OWLDeclaration, OWLFullClass, OWLFullIndividual, OWLLiteral, OWLOntology
from rdflib import XSD, Literal, Namespace, URIRef
from conftest import run_conversion_and_validation

def create_choquet_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_choquet#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    a_class = OWLFullClass(IRI(namespace, "A"))
    b_class = OWLFullClass(IRI(namespace, "B"))

    choquet_class = OWLFullClass(IRI(namespace, "ChoquetAB"))
    choquet_xml = """
    <fuzzyOwl2 fuzzyType="concept">
        <Concept type="choquet">
            <Weights>
                <Weight>0.5</Weight>
                <Weight>1</Weight>
            </Weights>
            <Names>
                <Name>A</Name>
                <Name>B</Name>
            </Names>
        </Concept>
    </fuzzyOwl2>
    """
    choquet_assertion = OWLAnnotationAssertion(choquet_class.class_.iri, fuzzy_label, OWLLiteral(Literal(choquet_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), a_class, b_class, choquet_class, choquet_assertion])
    ontology.save(str(owl_path))

def test_choquet(test_setup_factory):
    print("\n--- Starting Choquet Test ---")
    converter, original_path, final_path = test_setup_factory("test_choquet", create_choquet_ontology)

    run_conversion_and_validation(converter, original_path, final_path)