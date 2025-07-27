from fuzzy_dl_owl2 import FuzzyOwl2ToFuzzyDL
from fuzzy_dl_owl2 import FuzzydlToOwl2

class Converter:
    def __init__(self, owl_file, fdl_file):
        self.owl_file = owl_file
        self.fdl_file = fdl_file

        def translate_owl2_to_fdl(self):
            fdl = FuzzyOwl2ToFuzzyDL(self.owl_file, self.fdl_file)
            fdl.translate_owl2ontology()

        def translate_fdl_to_owl2(self, final_owl_file):
            fdl = FuzzydlToOwl2(self.fdl_file, final_owl_file)
            fdl.run()