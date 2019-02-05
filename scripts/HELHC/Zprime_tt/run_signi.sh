python python/significance.py -f "config_HELHC/Zprime_tt/helhc_v01/tagger_TC2_TRFbtag/Zprime_sel0_*TeV.config" -n Zprime_tt_TC2_helhc_v01_tagger_TRFbtag
python python/significance.py -f "config_HELHC/Zprime_tt/helhc_v01/tagger_SSM_TRFbtag/Zprime_sel0_*TeV.config" -n Zprime_tt_SSM_helhc_v01_tagger_TRFbtag

#
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/tt/Zprime_sel0_*TeV.config" -n Zprime_tt_helhc_v01
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/bb/Zprime_sel0_*TeV.config" -n Zprime_bb_helhc_v01
python python/significance.py -f "config_HELHC/Zprime_models/helhc_v01/tagger_SSM_TRFbtag/qq/Zprime_sel0_*TeV.config" -n Zprime_qq_helhc_v01

