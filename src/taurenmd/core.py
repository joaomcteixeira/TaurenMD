"""Library wide core utils."""
import os
from pathlib import Path as _Path


class Path(type(_Path())):
    """
    Extends Python's `Path object`_ interface.

    .. _Path object: https://docs.python.org/3/library/pathlib.html
    """
    def str(self):
        """
        String version of Path.
        
        Returns
        -------
        str
           ``os.fspath(self)``.
        """
        return os.fspath(self)
    
    def myparents(self):
        """
        A list of the path parent folders.
    
        Returns
        -------
        list
            Parent paths. Name file or folder are excluded.
        """
        return self.resolve().parents[0]


ref_taurenmd = "* Cite taurenmd according to: https://taurenmd.readthedocs.io/en/latest/citing.html\n"
"""How to cite taurenmd project."""

ref_mdt = "* MD data is accessed and/or processed using `MDTraj <https://mdtraj.org/>`_."
"""Command-line docstring to reference MDTraj package."""

ref_mda = "* MD data is accessed using `MDAnalysis <https://www.mdanalysis.org>`_.\n"
"""Command-line docstring to reference MDAnalysis package."""

ref_mda_selection = "* selection commands follow MDAnalysis `selection nomenclature <https://www.mdanalysis.org/docs/documentation_pages/selections.html#>`_.\n"
"""Command-line docstring to reference MDAnalysis selection commands."""

ref_mda_unwrap = "* unwrap performed by MDAnalysis `unwrap <https://www.mdanalysis.org/docs/documentation_pages/core/groups.html?highlight=unwrap#MDAnalysis.core.groups.AtomGroup.unwrap>`_.\n"
"""Command-line docstring to reference MDAnalysis selection.unwrap method."""

ref_mda_alignto = "* align performed by MDAnalysis `unwrap <https://www.mdanalysis.org/docs/documentation_pages/analysis/align.html?highlight=alignto#MDAnalysis.analysis.align.alignto>`_.\n"
"""Command-line docstring to reference MDAnalysis alignto function."""

ref_plottemplates_param = "* plotting is performed by `python-bioplottemplates plot param function <https://python-bioplottemplates.readthedocs.io/en/latest/reference/plots.html#bioplottemplates.plots.param.plot>`_.\n"
"""Command-line docstring to reference python-bioplottemplates param plot."""

ref_plottemplates_labeldots = "* plotting is performed by `python-bioplottemplates plot labeldots function <https://python-bioplottemplates.readthedocs.io/en/latest/reference/plots.html#bioplottemplates.plots.label_dots.plot>`_.\n"
"""Command-line docstring to reference python-bioplottemplates labeldots plot."""

ref_pyquaternion = "* Quaterion operations are performed with `pyquaterion <http://kieranwynn.github.io/pyquaternion/>`_.\n"
"""Command-line docstring to reference pyquaterion lib."""

