python python/limitplot.py -f "Outputs/helhc_v01/Zprime/tt/Zprime_tt_*TeV/Limits/*" -n "Zprime_tt_helhc_v01" -p "Z\' \rightarrow t\,\\wwbar{t}" -s "p8_pp_Zprime_VALUETeV_ttbar"

#
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/tt/Zprime_tt*TeV/Limits/*" -n "Zprime_tt_helhc_v01_allxs" -p "Z\' \rightarrow t\,\\wwbar{t}" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/bb/Zprime_bb*TeV/Limits/*" -n "Zprime_bb_helhc_v01_allxs" -p "Z\' \rightarrow b\,\\wwbar{b}" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"
python python/limitplot.py -f "Outputs/helhc_v01/Zprime_SSM/qq/Zprime_qq*TeV/Limits/*" -n "Zprime_qq_helhc_v01_allxs" -p "Z\' \rightarrow q\,\\wwbar{q}" -s "p8_pp_ZprimeSSM_VALUETeV_jj" -m "p8_pp_ZprimeCHI_VALUETeV_jj p8_pp_ZprimePSI_VALUETeV_jj p8_pp_ZprimeI_VALUETeV_jj p8_pp_ZprimeETA_VALUETeV_jj p8_pp_ZprimeLRM_VALUETeV_jj"

