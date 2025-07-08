# Fuzzy DL and OWL2 Conversion Testing

This project provides tools for converting ontologies between the OWL2 format and Fuzzy Description Logic (FuzzyDL). It also includes a script to validate the consistency of the conversion by comparing the original ontology with the reconverted one.

## Description

The project consists of three main parts:

1.  **Configuration (`CONFIG.ini`):** A file for setting the global parameters of the scripts.
2.  **Validation (`validate_conversion.py`):** A script to compare two ontologies (original and converted) and verify that the classes, properties, individuals, and axioms match.

-----

## Usage

### Conversion

The `converter.py` script is used for translation. Inside the file, the main functions are `translate_owl2_to_fdl` and `translate_fdl_to_owl2`.

To perform a conversion, you can modify and run the script directly. For example, to convert an OWL file to FuzzyDL:

```python
if __name__ == '__main__':
    translate_owl2_to_fdl("./results/persona.owl", "persona.fdl")
```

### Validation

After converting an ontology back to its original format, you can use `validate_conversion.py` to ensure that there has been no loss of information.

The script compares:

  * **Classes**
  * **Properties**
  * **Individuals**
  * **Axioms**

-----

## Dependencies

For the project to work correctly, the following Python libraries are required:

  * **owlready2**
  * **fuzzy\_dl\_owl2** (the custom library used for the conversion logic)
