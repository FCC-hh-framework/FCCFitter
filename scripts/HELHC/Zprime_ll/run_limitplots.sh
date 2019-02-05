python python/limitplot.py -f "Outputs/helhc_v01/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_helhc_v01" -p "Z\' \rightarrow \mu^+\mu^-" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_helhc_v01" -p "Z\' \rightarrow e^+e^-" -s "p8_pp_ZprimeSSM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_helhc_v01" -p "Z\' \rightarrow l^+l^-\ (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll"

python python/limitplot.py -f "Outputs/helhc_v01/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_helhc_v01_allxs" -p "Z\' \rightarrow \mu^+\mu^-" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_helhc_v01_allxs" -p "Z\' \rightarrow e^+e^-" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_helhc_v01_allxs" -p "Z\' \rightarrow l^+l^-\ (l=e,\mu)" -s "p8_pp_ZprimeSSM_VALUETeV_ll" -m "p8_pp_ZprimeCHI_VALUETeV_ll p8_pp_ZprimePSI_VALUETeV_ll p8_pp_ZprimeI_VALUETeV_ll p8_pp_ZprimeETA_VALUETeV_ll p8_pp_ZprimeLRM_VALUETeV_ll"

python python/limitplot.py -f "Outputs/helhc_v01/Zprime_ano/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_ano_helhc_v01" -p "Z\' \rightarrow \mu^+\mu^- (1710.06363)" -s "mgp8_pp_Zprime_mumu_5f_Mzp_VALUETeV"

