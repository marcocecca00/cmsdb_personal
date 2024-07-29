# coding: utf-8

"""
Higgs datasets for the 2022preEE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_hlep_rare import campaign_run3_2022_preEE_hlep_rare as cpn

cpn.add_dataset(
    name="h_ggf_htt",
    id=14805985,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHTo2Tau_UncorrelatedDecay_Filtered",  # noqa
            ],
            n_files=1,
            n_events=9999,
        ),
    ),
)
