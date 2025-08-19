from pyowl2 import IRI, OWLAnnotationAssertion, OWLAnnotationProperty, OWLClass, OWLClassAssertion, OWLDeclaration, OWLFullClass, OWLFullIndividual, OWLLiteral, OWLOntology
from rdflib import XSD, Literal, Namespace, URIRef
from conftest import run_conversion_and_validation

def create_quasi_sugeno_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_quasi_sugeno#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference)
    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    a_class = OWLFullClass(IRI(namespace, "A"))
    b_class = OWLFullClass(IRI(namespace, "B"))

    quasi_sugeno_class = OWLFullClass(IRI(namespace, "QuasiSugenoAB"))
    quasi_sugeno_xml = """
    <fuzzyOwl2 fuzzyType="concept">
        <Concept type="quasisugeno">
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
    quasi_sugeno_ass = OWLAnnotationAssertion(quasi_sugeno_class.class_.iri, fuzzy_label, OWLLiteral(Literal(quasi_sugeno_xml, datatype=XSD.string)))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), a_class, b_class, quasi_sugeno_class, quasi_sugeno_ass])
    ontology.save(str(owl_path))

def test_quasi_sugeno(test_setup_factory):
    print("\n--- Starting Quasi Sugeno Test ---")
    converter, original_path, final_path = test_setup_factory("test_quasi_sugeno", create_quasi_sugeno_ontology)

    run_conversion_and_validation(converter, original_path, final_path)