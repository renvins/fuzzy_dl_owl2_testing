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

---

### 2. Fuzzy Concept Constructors (Failures)

* **Weighted Sum Concept**
    * **Test File**: `weighted_sum_test.owl`
    * **Status**: ❌ **FAILED**
    * **Observations**: The converter ignored the `type="weightedSum"` annotation, suggesting the feature is not implemented.

* **Fuzzy Modifier**
    * **Test File**: `modifier_test.owl`
    * **Status**: ❌ **FAILED**
    * **Observations**: The converter ignored the `type="modified"` annotation. This feature also appears to be unimplemented.

* **Fuzzy Datatype in Restrictions**
    * **Test File**: `fuzzy_datatype_test.owl`
    * **Status**: ❌ **FAILED (CRASH)**
    * **Observations**: The conversion fails with a `FuzzyOntologyException`, indicating that the library does not support custom datatypes in `DataSomeValuesFrom` restrictions.