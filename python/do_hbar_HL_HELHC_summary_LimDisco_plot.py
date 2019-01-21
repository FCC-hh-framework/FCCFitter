# use root versio from 18/01/2019 to have dashed HBAR draw options:
# https://root-forum.cern.ch/t/draw-y-axis-histograms-hbar-option-not-satisfying/32307/15
# -> done on David's local machine for the moment

import ROOT as r

old_root=False
#old_root=True

raw_database=[]
#                           ana string 15 ab-1               / [disc, lim ]/ [disc, lim ] / 1=use the ana
#                                                                HL-LHC       HE-LHC
#spint 0 or 2
raw_database.append(["KK #rightarrow HH #rightarrow 4b",       [-1. ,  2. ], [-1. , -1. ], 1]) # ATLAS k/M=0.5 (6.1.1)
raw_database.append(["KK #rightarrow HH #rightarrow 4b",       [-1. , 2.75], [-1. , -1. ], 0]) # ATLAS k/M=1 (6.1.1)
raw_database.append(["KK #rightarrow HH #rightarrow 4b",       [-1. , 2.15], [-1. , -1. ], 0]) # ATLAS k/M=0.5 other BG scaling (6.1.1)
raw_database.append(["KK #rightarrow HH #rightarrow 4b",       [-1. , 2.95], [-1. , -1. ], 0]) # ATLAS k/M=1 other BG scaling (6.1.1)
raw_database.append(["KK #rightarrow HH #rightarrow 4b",       [ 2. , -1. ], [-1. , -1. ], 0]) # CMS k/M=0.5, 2.6 sigma (6.1.2)
#spint 1
raw_database.append(["Z\'_{SSM} #rightarrow #tau^{+}#tau^{-}", [-1. , -1. ], [ 6.5,  6.5], 1]) # HE (6.2.4)
raw_database.append(["Z\'_{f.a.} #rightarrow #mu^{+}#mu^{-}",  [-1  , -1. ], [ 1. ,  4. ], 0]) # HE f.a. = 1710.06363
raw_database.append(["Z\'_{SSM} #rightarrow l^{+}l^{-}",       [ 6.4, 6.5 ], [13. , 12.5], 1]) # ATLAS (6.2.5), HE (6.2.4)
raw_database.append(["Z\'_{TC2} #rightarrow t#bar{t}",         [-1. ,  4. ], [ 8. , 10. ], 1]) # ATLAS (6.2.3)
raw_database.append(["G_{RS} #rightarrow t#bar{t}",            [ 5.7,  6.6], [ 9.4, 10.7], 1]) # CMS (6.2.2)
raw_database.append(["W\'_{SSM} #rightarrow l#nu",             [ 7.7,  7.9], [-1. , -1. ], 1]) # ATLAS (6.2.6)
#spint 1/2
raw_database.append(["l* #rightarrow l^{+}l^{-} + #gamma",     [ 5.1,  5.8], [-1. , -1. ], 1]) # CMS (6.3.1)
# signature base
raw_database.append(["G_{RS} #rightarrow W^{+}W^{-}",          [-1. , -1. ], [ 7. ,  8. ], 1]) # HE (6.4.6)
raw_database.append(["Z\'_{SSM} #rightarrow t#bar{t}",         [-1. , -1. ], [ 6. ,  8. ], 1]) # HE (6.4.6)
raw_database.append(["Q* #rightarrow jj",                      [-1. , -1. ], [12. , 14. ], 1]) # HE (6.4.6)
raw_database.append(["HVT  #rightarrow VV",                    [ 5.8,  5. ], [-1. , 11. ], 1]) # ATLAS (6.4.4)

#raw_database.append(["",   [ , ], [ , ], ])

database=[]
for i in raw_database:
  if i[3]==1 : database.append([i[0], [i[1][1], i[1][0]], [i[2][1], i[2][0]]])

nAna=len(database)
my_hist=[]
my_hist.append( r.TH1F("limit_HL", "limit_HE", nAna,0.,nAna)) # limit HE
my_hist.append( r.TH1F("limit_HE", "limit_HL", nAna,0.,nAna)) # limit HL
my_hist.append( r.TH1F("disco_HL", "disco_HE", nAna,0.,nAna)) # disco HE
my_hist.append( r.TH1F("disco_HE", "disco_HL", nAna,0.,nAna)) # disco HL

#color  = [r.kYellow-7, r.kRed+1, r.kGreen+3, r.kBlue+1]
#color  = [r.kAzure-9, r.kBlue+1, r.kGreen+3, r.kBlack]
color  = [r.kAzure-9, r.kGreen-9, r.kGreen+3, r.kRed-2]
legend = [
"#splitline{HE-LHC}{#scale[0.75]{#it{#sqrt{s} = 14 TeV}, #it{L = 3 ab^{-1}}}}",
"#splitline{HL-LHC}{#scale[0.75]{#it{#sqrt{s} = 27 TeV}, #it{L = 15 ab^{-1}}}}"
]

process = []
for i in range(nAna): process.append(database[i][0])
val_HL   = []
for i in range(nAna): val_HL.append(database[i][1])
val_HE   = []
for i in range(nAna): val_HE.append(database[i][2])

#count_ana = 0
for i_bin in range(nAna):
  my_hist[0].SetBinContent(i_bin+1, val_HE[i_bin][0])
  my_hist[1].SetBinContent(i_bin+1, val_HL[i_bin][0])
  my_hist[2].SetBinContent(i_bin+1, val_HE[i_bin][1])
  my_hist[3].SetBinContent(i_bin+1, val_HL[i_bin][1])
  #
  str_proc = '#scale[1.02]{#font[22]{'+process[i_bin]+'}}'
  my_hist[0].GetXaxis().SetBinLabel(i_bin+1,str_proc)

my_hist[0].SetBarWidth(0.8)
my_hist[0].SetLineColorAlpha(color[0],0.)
my_hist[0].SetFillColorAlpha(color[0],0.8)
my_hist[0].SetMarkerColorAlpha(color[0],0.)
my_hist[1].SetBarWidth(0.8)
my_hist[1].SetLineColorAlpha(color[1],0.)
my_hist[1].SetFillColorAlpha(color[1],0.9)
my_hist[1].SetMarkerColorAlpha(color[1],0.)
if old_root==True :
  my_hist[2].SetBarWidth(0.7)
  my_hist[2].SetLineColorAlpha(color[2],0.)
  my_hist[2].SetFillColorAlpha(color[2],0.7)
  my_hist[2].SetMarkerColorAlpha(color[2],0.)
  my_hist[2].SetFillStyle(3465)
  my_hist[3].SetBarWidth(0.6)
  my_hist[3].SetLineColorAlpha(color[3],0.)
  my_hist[3].SetFillColorAlpha(color[3],0.7)
  my_hist[3].SetMarkerColorAlpha(color[3],0.)
  my_hist[3].SetFillStyle(3351)
else :
  my_hist[2].SetBarWidth(0.7)
  my_hist[2].SetFillStyle(0)
  my_hist[2].SetLineWidth(3)
  my_hist[2].SetLineColor(color[2])
  my_hist[2].SetLineStyle(r.kDashed)
  my_hist[3].SetBarWidth(0.6)
  my_hist[3].SetFillStyle(0)
  my_hist[3].SetLineWidth(3)
  my_hist[3].SetLineColor(color[3])
  my_hist[3].SetLineStyle(r.kDashed)

canvas = r.TCanvas("test", "test", 600, 600)
canvas.SetTicks(1,1)
canvas.SetLeftMargin(0.21)
canvas.SetRightMargin(0.02)
r.gStyle.SetOptStat(0)
r.gPad.SetGridx()

x_len=0.25
y_len=0.18
#
x_low=0.55
y_low=0.72
leg_x=[x_low,y_low,x_low+x_len,y_low+y_len]
#
x_low=0.65
y_low=0.52
leg_y=[x_low,y_low,x_low+x_len,y_low+y_len]
#
leg_coor=[]
for i in range(len(leg_y)): leg_coor.append(leg_y[i])

leg = r.TLegend(leg_coor[0],leg_coor[1],leg_coor[2],leg_coor[3])
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetLineColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.035)
leg.SetTextFont(42)

leg2 = r.TLegend(leg_coor[0],leg_coor[1],leg_coor[2],leg_coor[3])
leg2.SetFillColor(0)
leg2.SetFillStyle(0)
leg2.SetLineColor(0)
leg2.SetShadowColor(10)
leg2.SetTextSize(0.035)
leg2.SetTextFont(42)

the_max=max(my_hist[0].GetMaximum(),my_hist[1].GetMaximum(),my_hist[2].GetMaximum(),my_hist[3].GetMaximum())
my_hist[0].SetMinimum(0.)
my_hist[0].SetMaximum(the_max*1.1)
my_hist[0].SetTitle("")
my_hist[0].GetYaxis().SetTitleOffset(1.30)
my_hist[0].GetYaxis().SetTitle("Mass scale [TeV]")
my_hist[0].GetXaxis().SetLabelSize(0.045)
my_hist[0].GetXaxis().SetTickLength(0.)

my_hist[0].Draw("HBAR")
my_hist[1].Draw("HBARsame")
my_hist[2].Draw("HBARsame")
my_hist[3].Draw("HBARsame")

leg.AddEntry(my_hist[0],legend[0])
leg.AddEntry(my_hist[1],legend[1])
leg2.AddEntry(my_hist[2],legend[0])
leg2.AddEntry(my_hist[3],legend[1])
leg.Draw("same")
leg2.Draw("same")

Text = r.TLatex()
Text.SetNDC()

leftText = "95% CL Limit (solid), 5 #sigma Discovery (dash)"
if old_root==True : leftText = "95% CL Limit (solid), 5 #sigma Discovery (hatching)"
Text.SetTextAlign(31);
Text.SetTextSize(0.04)
Text.DrawLatex(0.97, 0.92, '#it{' + leftText +'}')

canvas.RedrawAxis()
canvas.RedrawAxis("g");
canvas.GetFrame().SetBorderSize( 12 )
canvas.Update()
canvas.Modified()

canvas.Print("summaryLimDisco_HL_HELHC.pdf")

