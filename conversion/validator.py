from owlready2 import *

class Validator:
    def __init__(self, original_path, final_path):
        self.original_onto = get_ontology(original_path).load()
        self.final_onto = get_ontology(final_path).load()

    def compare_classes(self):
        # Check if the classes in both ontologies are the same
        original_classes = {c.name for c in self.original_onto.classes()}
        final_classes = {c.name for c in self.final_onto.classes()}

        assert original_classes == final_classes, f"Classes do not match! Original: {original_classes}, Final: {final_classes}"
        print("✅ Classes match.")

    def compare_properties(self):
        # Check if the properties in both ontologies are the same
        original_properties = {p.name for p in self.original_onto.properties()}
        final_properties = {p.name for p in self.final_onto.properties()}

        assert original_properties == final_properties, f"Properties do not match! Original: {original_properties}, Final: {final_properties}"
        print("✅ Properties match.")

    def compare_individuals(self):
        # Check if the individuals in both ontologies are the same
        original_individuals = {i.name for i in self.original_onto.individuals()}
        final_individuals = {i.name for i in self.final_onto.individuals()}

        assert original_individuals == final_individuals, f"Individuals do not match! Original: {original_individuals}, Final: {final_individuals}"
        print("✅ Individuals match.")

    def compare_axioms(self):
        # This is the most important part, checking if the axioms are the same
        original_axioms = list(self.original_onto.general_class_axioms())
        final_axioms = list(self.final_onto.general_class_axioms())

        assert original_axioms == final_axioms, f"Axioms do not match! Original: {original_axioms}, Final: {final_axioms}"
        print("✅ Axioms match.")