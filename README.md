# Conversion Tests for fuzzy\_dl\_owl2

This repository contains a set of test ontologies to validate and analyze the behavior of the `fuzzy_dl_owl2` library. The goal is to verify the correct translation of OWL 2 constructs with fuzzy annotations into the FuzzyDL format and vice versa.

The library is designed to interoperate between the standard OWL 2 ontology language and the FuzzyDL reasoner, allowing you to leverage fuzzy reasoning capabilities while maintaining compatibility with the OWL ecosystem.

## How to Run the Tests

To verify the correct functioning of the conversion and validate all test ontologies, simply run the following command from the main project directory:

```bash
python -m pytest -v -s
```

This command will automatically discover and run all the tests defined in the `tests/` directory, providing a detailed report of any successes or failures. Each test handles creating an OWL ontology, converting it to FuzzyDL, converting it back to OWL, and finally comparing the original ontology with the final one to ensure their equivalence.
