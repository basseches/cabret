#!/usr/bin/env python3

import os

from texonomy.texonomy import *

journal = Entity("Journal", ["name", "ISBN number", "title", "pub freq", \
                                "subscription price"])
journal.set_primary("ISBN number")
editor = Entity("Editor-in-chief", ["name", "personal affiliation", \
                                    "email"])
editor.set_primary("email")
issue = Entity("Issue", ["issue-num"], True)
article = Entity("Article", ["doi-identifier", "title", "page range"])
author = Entity("Author", ["name", "author-id"])
author.set_primary("author-id")
contact_author = Entity("Contact author", ["contact email"])

diag = ERDiagram(journal)

diag.add_relationship(Relationship(journal, editor, "edited-by", \
                                    MANY_TO_EXACTLY_ONE, Direction.RIGHT))
diag.add_relationship(Relationship(journal, issue, "issues", \
                                    EXACTLY_ONE_TO_MANY, Direction.BELOW, \
                                    ["publication-date"]), True)
diag.add_relationship(Relationship(issue, article, "contains", \
                                    ((1, -1), (1, 1)), Direction.RIGHT))
diag.add_relationship(Relationship(article, author, "authored-by", \
                                    ((1,-1), (0,-1)), Direction.BELOW))
diag.add_specialization(author, contact_author)

with open("journal.tex", "w") as er:
    er.write(diag.to_latex("template.tex"))

os.system("pdflatex journal.tex")
