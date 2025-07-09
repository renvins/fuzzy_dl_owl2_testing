from fuzzy_dl_owl2 import FuzzyOwl2ToFuzzyDL
from fuzzy_dl_owl2 import FuzzydlToOwl2

def translate_owl2_to_fdl(owl_file, fdl_file):
    fdl = FuzzyOwl2ToFuzzyDL(owl_file, fdl_file)
    fdl.translate_owl2ontology()

def translate_fdl_to_owl2(fdl_file, owl_file):
    fdl = FuzzydlToOwl2(fdl_file, owl_file)
    fdl.run()

if __name__ == '__main__':
    print("Starting translations...")
    #translate_owl2_to_fdl("./results/persone_fuzzy.owl", "persone_fuzzy.fdl")
    #translate_fdl_to_owl2("./results/persone_fuzzy.fdl", "persone_fuzzy_final.owl")