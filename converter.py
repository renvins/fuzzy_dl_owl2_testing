from fuzzy_dl_owl2 import FuzzyOwl2ToFuzzyDL
from fuzzy_dl_owl2 import FuzzydlToOwl2

def translate_owl2_to_fdl(owl_file, fdl_file):
    fdl = FuzzyOwl2ToFuzzyDL(owl_file, fdl_file)
    fdl.translate_owl2ontology()

def translate_fdl_to_owl2(fdl_file, owl_file):
    fdl = FuzzydlToOwl2(fdl_file, owl_file)
    fdl.run()

if __name__ == '__main__':
    translate_owl2_to_fdl("./results/persona.owl", "persona.fdl")
    #translate_fdl_to_owl2("./results/persona.fdl", "persona2.owl")