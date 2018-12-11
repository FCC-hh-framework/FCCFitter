python python/limitplot.py -f "Outputs/fcc_v02/Zprime/tt/Zprime_tt_*TeV/Limits/*" -n "Zprime_tt_fcc_v02" -p "Z\' \rightarrow tt" -s "p8_pp_Zprime_VALUETeV_ttbar"

python python/limitplot.py -f "Outputs/fcc_v02/Zprime/tt/Zprime_tt_*TeV/Limits/*" -n "Zprime_tt_fcc_v02_degrade" -p "Z\' \rightarrow tt" -s "p8_pp_Zprime_VALUETeV_ttbar" --degrade1 "Outputs/fcc_v02/Zprime/tt_degrade_1/Zprime_tt_*TeV/Limits/*" --degrade2 "Outputs/fcc_v02/Zprime/tt_degrade_2/Zprime_tt_*TeV/Limits/*" --degrade3 "Outputs/fcc_v02/Zprime/tt_degrade_3/Zprime_tt_*TeV/Limits/*"
