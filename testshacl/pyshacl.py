import os
from os.path import exists
from rdflib import Graph
from pathlib import Path
import pyshacl
import sys

def run(folder: Path):
    datafile = folder / "data.ttl"
    shapefile = folder / "shapes.ttl"

    datagraph = Graph().parse(datafile)
    shapegraph = Graph().parse(shapefile)

    valid, report_graph, report_str = pyshacl.validate(datagraph, shacl_graph=shapegraph,
                                                       ont_graph=shapegraph, advanced=True,
                                                       allow_infos=True, inplace=True)
    os.makedirs(folder / "pyshacl", exist_ok=True)
    print(f"Test case {folder} valid?: {valid}")
    with open(folder / "pyshacl" / "report.txt", "w") as f:
        f.write(report_str)
    report_graph.serialize(folder / "pyshacl" / "report.ttl")


def main():
    if len(sys.argv) < 2:
        print("Usage: pyshacl <test case directory>")
        sys.exit(1)
    run(Path(sys.argv[1]))
