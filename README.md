# Conversion Tests for fuzzy_dl_owl2

This repository contains a set of test ontologies to validate and analyze the behavior of the `fuzzy_dl_owl2` library. The goal is to verify the correct translation of OWL 2 constructs with fuzzy annotations into the FuzzyDL format.

---

## Test Summary

Below is a list of the tests performed, with the corresponding ontology files and the results obtained.

### 1. Standard Axioms (Successes)

* **Axiom with Truth Degree**
    * **Test File**: `axiom_test.owl`
    * **Status**: ✅ **SUCCESS**
    * **Observations**: The library correctly interpreted the `<Degree value="..."/>` annotation on a `ClassAssertion` axiom.

* **Disjoint Classes**
    * **Test File**: `disjoint_test.owl`
    * **Status**: ✅ **SUCCESS**
    * **Observations**: The library correctly parsed and translated the `DisjointWith` axiom between two classes.

* **Subclasses**
    * **Test File**: `subclass_test.owl`
    * **Status**: ✅ **SUCCESS**
    * **Observations**: The library correctly parsed and translated the `SubclassOf` axiom between two classes.

---

### 2. Fuzzy Concept Constructors

* **Fuzzy Datatype in Restrictions**
    * **Test File**: `fuzzy_datatype_test.owl`
    * **Status**: ✅ **SUCCESS**
    * **Observations**: Successfully converted the `FuzzyDatatype` concept, including the trapezoidal function in the restriction.

* **Weighted Sum Concept**
    * **Test File**: `weighted_sum_test.owl`
    * **Status**: ❌ **FAILED**
    * **Observations**: Successfully converted the `WeightedSum` concept, but conversion fdl -> owl2 failed
    * **Errors**: [Link to the error, related to syntax probably](https://pastebin.com/R1Wn6Vvp)

* **Fuzzy Modifier**
    * **Test File**: `modifier_test.owl`
    * **Status**: ❌ **FAILED**
    * **Observations**: Successfully converted the `FuzzyModifier` concept, but conversion fdl -> owl2 was missing classes
    * **Errors**: [This is what the conversion validator reported](https://pastebin.com/Ftb5xHvp)
 
---

### 3. Not supported yet

* **Fuzzy Nominals**
    * **Test File**: `nominal_test.owl`
    * **Status**: ❌ **FAILED**
    * **Observations**: Throws error due to feature not supported
