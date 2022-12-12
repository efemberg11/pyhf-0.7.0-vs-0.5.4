import os
import pyhf.readxml
from pathlib import Path
import matplotlib.pyplot as plt
import time

import cabinetry

begin_o = time.time()

chanal = [  'three_lep_presel_1jet'
            #'SR_WVZ_NJ1',
            #'SR_WVZ_NJ2',
            #'SR_WVZ_NJ3'
            ]#, 'ttZ_3L_CR']
meas_name = 'Full_fit'
#meas_name = 'Full_fit'
spec = pyhf.readxml.parse(meas_name+'/RooStats/'+meas_name+'.xml', Path.cwd())
spec["channels"] = [c for c in spec["channels"] if c["name"] in chanal]

w = pyhf.Workspace(spec)

model, data = cabinetry.model_utils.model_and_data(w)

fit_results = cabinetry.fit.fit(model, data, minos=model.config.poi_name, custom_fit=True, tolerance=0.01, maxiter = 30000)

for idx in range(len(fit_results.labels)):
        print(f' {idx} {fit_results.labels[idx]} {fit_results.bestfit[idx]:.7f}+-{fit_results.uncertainty[idx]:.5f}')


ranking_res = cabinetry.fit.ranking(model, data,custom_fit=True, tolerance = 0.01, maxiter = 30000)# maxiter=50000, strategy = 1, )
for idx in range(len(ranking_res.labels)):
       #print('ranking')
       print(f' {idx} {ranking_res.labels[idx]} {ranking_res.bestfit[idx]:.7f} +- {ranking_res.uncertainty[idx]:.5f} post_dn {ranking_res.postfit_down[idx]:.5f} post_up {ranking_res.postfit_up[idx]:.5f}  pre_dn {ranking_res.prefit_down[idx]:.5f} pre_up {ranking_res.prefit_up[idx]:.5f}')

# #rank_fig_asimov = cabinetry.visualize.ranking(ranking_res_asimov)
# rank_fig = cabinetry.visualize.ranking(ranking_res)

# rank_fig.savefig('ranking_plt2.png')
# #rank_fig_asimov.savefig('/share/users/ramdas/PHF_ishxonasi/TRexProblem/figures/ranking_asimov_plt.png')

stop = time.time()
dif = stop-begin_o
print('plotting time is:    ', dif)
