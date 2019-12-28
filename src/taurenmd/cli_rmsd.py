"""
Does something.
"""
import argparse
import functools
from datetime import datetime

import numpy as np
from bioplottemplates.plots import param

from taurenmd import Path, log
from taurenmd.libs import libcalc, libcli, libmda, libio
from taurenmd.logger import S, T

_help = 'Calculates and plots RMSDs.'
_name = 'rmsd'

ap = libcli.CustomParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    )

libcli.add_topology_arg(ap)
libcli.add_trajectories_arg(ap)
libcli.add_atom_selections_arg(ap)
libcli.add_reference_frame_arg(ap)
libcli.add_slice_arg(ap)
libcli.add_data_export_arg(ap)
libcli.add_plot_arg(ap)


def main(
        topology,
        trajectories,
        start=None,
        stop=None,
        step=None,
        ref_frame=0,
        selections=None,
        plot=False,
        plotvars=None,
        export=False,
        **kwargs
        ):
    """Main client logic."""
    log.info(T('starting'))
    
    u = libmda.load_universe(topology, *trajectories)
    
    frame_slice = libio.frame_slice(
        start=start,
        stop=stop,
        step=step,
        )
    
    if selections is None:
        selections = ['all']
    rmsds = []
    for selection in selections:
        rmsds.append(
            libcalc.mda_rmsd(
                u,
                frame_slice=frame_slice,
                selection=selection,
                ref_frame=ref_frame,
                )
            )
    if export:
        np.savetxt(
            export,
            np.array([range(len(u.trajectory))[frame_slice]] + rmsds).T,
            fmt=['%d'] + ['%.5e'] * len(rmsds),
            delimiter=',',
            newline='\n',
            header=(
                "Date: {}\n'"
                "Topology: {}\n"
                "Trajectory : {}\n"
                "ref frame: {}\n"
                "frame number, {}\n"
                ).format(
                    datetime.now(),
                    Path(topology).resolve(),
                    [Path(f).resolve().str() for f in trajectory],
                    ','.join(selections),
                    ref_frame,
                    ),
            footer='',
            comments='#',
            encoding=None,
            )
    
    if plot:

        plotvars = plotvars or dict()
        plotvars.setdefault('labels', selections)

        log.info(T('plot params:'))
        for k, v in plotvars.items():
            log.info(S('{} = {!r}', k, v))
        
        param.plot(
            list(range(len(u.trajectory))[frame_slice]),
            rmsds,
            **plotvars,
            )

    return


maincli = functools.partial(libcli.maincli, ap, main)


if __name__ == '__main__':
    maincli()
