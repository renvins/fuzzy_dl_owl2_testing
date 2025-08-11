from fuzzy_dl_owl2 import FuzzyOwl2ToFuzzyDL
from fuzzy_dl_owl2 import FuzzydlToOwl2
from pathlib import Path

class Converter:
    def __init__(self, owl_file: Path, fdl_file: Path):
        self.owl_file = owl_file
        self.fdl_file = fdl_file

    def translate_owl2_to_fdl(self):
        fdl = FuzzyOwl2ToFuzzyDL(str(self.owl_file), str(self.fdl_file))
        fdl.translate_owl2ontology()

    def translate_fdl_to_owl2(self, final_owl_file: Path):
        fdl = FuzzydlToOwl2(str(self.fdl_file), str(final_owl_file))
        fdl.run()