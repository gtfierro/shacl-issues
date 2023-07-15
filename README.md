# shacl-issues

Documenting issues with SHACL and variations in SHACL output.

## Structure

- `/ontologies/`: a folder for each ontology referenced in the repo; folder should also contain all of the dependencies for the ontology
- `/scripts/`: supplementary tools for interacting with ontologies and other parts of the repo:
    - `./scripts/update_ontologies.sh`: run this to update the local cache of all ontologies
- `/testcases/`: contains folders, each with a different SHACL validation or inference scenario:
    - each testcase has 2 files: `data.ttl` containing data to be run through inference or validation,
      and `shapes.ttl` containing the SHACL shapes to perform that inference or validation

## SHACL Implementations

There are two implementations available:
- https://github.com/RDFLib/pySHACL
- https://github.com/TopQuadrant/shacl

These are abstracted behind simple Python wrappers in the `testshacl` package in this repo

## Running Testcases

*Note: be sure to run the `./build-topbraid-shacl.sh` script from the `scripts/` directory. This will create a local Docker image for the TopQuadrant SHACL implementation*

Use `poetry` to run either the `pyshacl` or `topquadrant_shacl` script on a testcase directory:

- `poetry run pyshacl testcases/sh_or_ambiguity`
- `poetry run topquadrant_shacl testcases/sh_or_ambiguity`
