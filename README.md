# texonomy

`texonomy`* is a Python tool that facilitates the generation of
entity-relationship diagrams in $\LaTeX$ using TikZ.

[![License](https://img.shields.io/github/license/basseches/texonomy)](https://github.com/basseches/texonomy)
[![Build Status](https://github.com/basseches/texonomy/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/basseches/texonomy/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/basseches/texonomy/branch/main/graph/badge.svg)](https://codecov.io/gh/basseches/texonomy)

## Overview

Writing $\LaTeX$ code can be tedious; `texonomy` makes it easier. This tool
generates entity-relationship diagrams in $\LaTeX$ using a beginner-friendly
Python interface, so you can spend less time wrestling with missing semicolons.

In order to output as a PDF, you'll need to install some software that includes
`pdflatex`, like TeX Live.

*An entity-relationship diagram is more of an ontology than a taxonomy, but
when the shoe fits...

## Testing

For the unit tests, run `make test` or `make coverage` (for coverage report) at
the top-level directory. For the integration tests, run `make test` in
`texonomy/tests/integration_tests`. The output will be stored in
`texonomy/tests/integration_tests/pdf` and
`texonomy/tests/integration_tests/tex`.

## Linting and formatting

Run `make lint` at the top-level directory to lint, and `make format` to
format.
