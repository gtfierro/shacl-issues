import os
import docker
from rdflib import Graph
from pathlib import Path
import pyshacl
import sys

def run(folder: Path):
    datafile = folder / "data.ttl"
    shapefile = folder / "shapes.ttl"
    os.makedirs(folder / "topquadrant_shacl", exist_ok=True)

    volume_bindings = {
        str(folder.absolute()): {
            'bind': '/data',
            'mode': 'rw'
        }
    }

    client = docker.from_env()
    command = "infer -shapefile /data/shapes.ttl -datafile /data/data.ttl"
    container = client.containers.run("ghcr.io/topquadrant/shacl:1.4.2", volumes=volume_bindings, command=command)
    print(container.decode('utf-8'))


def main():
    if len(sys.argv) < 2:
        print("Usage: topquadrant_shacl <test case directory>")
        sys.exit(1)
    run(Path(sys.argv[1]))
