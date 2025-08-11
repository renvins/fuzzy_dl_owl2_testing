from pyowl2 import OWLOntology, OWLFullClass, IRI, OWLAnnotationProperty, OWLDeclaration, OWLFullDataProperty, \
    OWLDatatype, OWLAnnotationAssertion, OWLLiteral, OWLFacet, OWLDatatypeRestriction, OWLDatatypeDefinition, \
    OWLDataSomeValuesFrom
from rdflib import URIRef, Namespace, Literal, XSD

from conftest import run_conversion_and_validation

def create_fuzzy_datatype_ontology(owl_path):
    reference = URIRef("https://www.semanticweb.org/vince/ontologies/2025/6/test_fuzzy_datatype#")
    namespace = Namespace(reference)

    ontology = OWLOntology(reference, OWL1_annotations=True)

    fuzzy_label = OWLAnnotationProperty(IRI(namespace, "fuzzyLabel"))

    # Here we define a class hierarchy where OldPerson is a subclass of Person
    person = OWLFullClass(IRI(namespace, "Person"))
    old_person = OWLFullClass(IRI(namespace, "OldPerson"))

    old_person.is_subclass_of(person)

    # Create the XSD namespace and integer datatype
    xsd_namespace = Namespace(str(XSD))
    integer_datatype = OWLDatatype(IRI(xsd_namespace, "integer"))

    # Define a data property that indicates the age of a person
    have_age = OWLFullDataProperty(IRI(namespace, "HaveAge"), range=integer_datatype, domain=person.class_)

    # Define a fuzzy datatype for old age
    old_age_datatype = OWLDatatype(IRI(namespace, "OldAge"))

    # Define the fuzzy datatype restriction for old age
    min_age = OWLFacet(XSD.minExclusive, OWLLiteral(Literal("54", datatype=XSD.integer)))
    max_age = OWLFacet(XSD.maxInclusive, OWLLiteral(Literal("100", datatype=XSD.integer)))

    # Create the old age restriction using the integer datatype and the defined facets
    old_age_restriction = OWLDatatypeRestriction(integer_datatype, restrictions=[min_age, max_age])

    # Define the old age datatype definition
    old_age_definition = OWLDatatypeDefinition(old_age_datatype, old_age_restriction)

    # Create the XML representation of the fuzzy datatype
    old_age_xml = "<fuzzyOwl2 fuzzyType=\"datatype\"><Datatype type=\"trapezoidal\" a=\"55\" b=\"65\" c=\"75\" d=\"85\"></Datatype></fuzzyOwl2>"
    old_age_annotation = OWLAnnotationAssertion(old_age_datatype.iri, fuzzy_label,
                                                OWLLiteral(Literal(old_age_xml, datatype=XSD.string)))

    old_person.is_equivalent_to(OWLDataSomeValuesFrom([have_age.data_property], old_age_datatype))

    ontology.add_axioms([OWLDeclaration(fuzzy_label), OWLDeclaration(old_age_datatype), person, old_person, have_age, old_age_definition, old_age_annotation])
    ontology.save(str(owl_path))

def test_fuzzy_datatype(test_setup_factory):
    print("\n--- Starting Fuzzy Datatype Test ---")
    converter, original_path, final_path = test_setup_factory("test_fuzzy_datatype", create_fuzzy_datatype_ontology)

    run_conversion_and_validation(converter, original_path, final_path)