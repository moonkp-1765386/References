from Peeves.Doc import *
import os

__pkgs__ = [
    "McUtils",
    "Psience",
    "Peeves",
    "PyDVR",
    "PyVPT",
    "RynDMC"
]

target = os.path.join(os.path.dirname(__file__), "Documentation")
DocWalker(__pkgs__, target).write_docs()