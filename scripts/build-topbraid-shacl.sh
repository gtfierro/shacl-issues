#!/bin/bash 
git clone https://github.com/TopQuadrant/shacl topquadrant_shacl_git
cd topquadrant_shacl_git && docker build -f .docker/Dockerfile -t ghcr.io/topquadrant/shacl:1.4.2 --build-arg VERSION=1.4.2 .
