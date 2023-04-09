Welcome to texonomy's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   examples
   documentation

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Overview
--------

Writing :math:`\LaTeX` code can be tedious; ``texonomy`` makes it
easier. This tool generates entity-relationship diagrams in
:math:`\LaTeX` using a beginner-friendly Python interface, so you can
spend less time wrestling with missing semicolons.

Example usage
~~~~~~~~~~~~~

Let’s create a very simple program with ``texonomy``. First, we’ll
create an Entity object to represent a fruit:

.. code:: py

   fruit = Entity("Fruit", ["SKU", "name", "price", "origin"])

The first argument is the entity’s name, “Fruit”. The second argument is
a list of the entity’s attributes.

Let’s create a diagram that contains our fruit entity…

.. code:: py

   diag = ERDiagram(fruit)

…and output the generated :math:`\LaTeX` to a file!

.. code:: py

   with open("fruit.tex", "w") as er:
       er.write(diag.to_latex())

Then, you can run ``pdflatex`` (or something similar) on the command
line to generate a PDF from this :math:`\LaTeX`:

.. code:: sh

   pdflatex fruit.tex

It’s that simple! Take a look at the programs on the examples page for more examples of API usage.
