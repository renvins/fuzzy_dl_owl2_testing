# Conversion Tests for fuzzy_dl_owl2

This repository contains a set of test ontologies to validate and analyze the behavior of the `fuzzy_dl_owl2` library. The goal is to verify the correct translation of OWL 2 constructs with fuzzy annotations into the FuzzyDL format.

---

## Test Summary

Below is a list of the tests performed, with the corresponding ontology files and the results obtained.

### 1. Axiom with Truth Degree (Degree)
* **Feature Tested**: Assertion of an individual's membership in a class with a numerical degree of truth.
* **Test File**: `persone_fuzzy.owl`
* **Status**: ✅ **SUCCESS**
* **Observations**: The library correctly interpreted the `<Degree value="..."/>` annotation on a `ClassAssertion` axiom, translating it to the FDL format and converting it back successfully.

---

### 2. Fuzzy Modifier
* **Feature Tested**: Definition of a "modifier" (e.g., `molto`) and its application to a class to create a modified version (e.g., `PersonaMoltoAlta`).
* **Test File**: `modifier_persona.owl`
* **Status**: ❌ **FAILED**
* **Observations**: The converter did not produce an error, but it generated an incomplete `.fdl` file, ignoring the `fuzzyType="modifier"` and `type="modified"` annotations. This suggests the feature is not yet implemented.

---

### 3. Fuzzy Datatype in Restrictions
* **Feature Tested**: Definition of a custom fuzzy datatype (e.g., `EtaAnziana`) and its use within an existential restriction (`haEta some EtaAnziana`).
* **Test File**: `persona_fuzzy_bug.owl`
* **Status**: ❌ **FAILED (CRASH)**
* **Observations**: The conversion fails with a `FuzzyOntologyException`, indicating that the library does not support the use of custom datatypes as a range in `DataSomeValuesFrom` restrictions.
