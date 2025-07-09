from owlready2 import *

def compare_classes(original_onto, final_onto):
    # Check if the classes in both ontologies are the same
    original_classes = {c.name for c in original_onto.classes()}
    final_classes = {c.name for c in final_onto.classes()}

    if original_classes == final_classes:
        print("Classes match between original and final ontologies.")
    else:
        print("Classes do not match:")
        print("Original classes:", original_classes)
        print("Final classes:", final_classes)

def compare_properties(original_onto, final_onto):
    # Check if the properties in both ontologies are the same
    original_properties = {p.name for p in original_onto.properties()}
    final_properties = {p.name for p in final_onto.properties()}

    if original_properties == final_properties:
        print("Properties match between original and final ontologies.")
    else:
        print("Properties do not match:")
        print("Original properties:", original_properties)
        print("Final properties:", final_properties)

def compare_individuals(original_onto, final_onto):
    # Check if the individuals in both ontologies are the same
    original_individuals = {i.name for i in original_onto.individuals()}
    final_individuals = {i.name for i in final_onto.individuals()}
    if original_individuals == final_individuals:
        print("Individuals match between original and final ontologies.")
    else:
        print("Individuals do not match:")
        print("Original individuals:", original_individuals)
        print("Final individuals:", final_individuals)

def compare_axioms(original_onto, final_onto):
    # This is the most important part, checking if the axioms are the same
    original_axioms = list(original_onto.general_class_axioms())
    final_axioms = list(final_onto.general_class_axioms())
    if original_axioms == final_axioms:
        print("Axioms match between original and final ontologies.")
    else:
        print("Axioms do not match:")
        print("Original axioms:", original_axioms)
        print("Final axioms:", final_axioms)

def validate_conversion(original_path, final_path):
    # Load the ontologies
    original_onto = get_ontology(original_path).load()
    final_onto = get_ontology(final_path).load()

    # Compare classes, properties, individuals, and axioms
    compare_classes(original_onto, final_onto)
    compare_properties(original_onto, final_onto)
    compare_individuals(original_onto, final_onto)
    compare_axioms(original_onto, final_onto)

if __name__ == "__main__":
    original_path = "./results/persone_fuzzy.owl"
    final_path = "./results/persone_fuzzy_final.owl"

    validate_conversion(original_path, final_path)