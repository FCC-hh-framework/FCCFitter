#####################################
# use root version from 18/01/2019 to have dashed HBAR draw options :
# https://root-forum.cern.ch/t/draw-y-axis-histograms-hbar-option-not-satisfying/32307/15
# -> done on David's local machine for the moment
# OK for ROOT>=6.18
#####################################
# numbers taken from HL-HE-LHC Physics WG3 Report NEW :
# https://www.overleaf.com/read/bwxpnwmshgdq
#####################################

import ROOT as r

#################################
show_section=True
#show_section=False

#################################
old_root=False
#old_root=True

arrow="\\rightarrow"
l="\\ell"
emu="("+l+"=e,\\mu)"
#
raw_database=[]
#                    ana  / [disc, lim , sec    ]/ [disc, lim , sec    ]/ order / spin
#                    str        HL-LHC                  HE-LHC      
#spin 0 or 2
title="KK"+arrow+"HH"+arrow+"4b"
raw_database.append([title, [-1. ,  2. , "6.1.1"], [-1. , -1. , "empty"], -1, 2. ]) # ATLAS k/M=0.5 (6.1.1)
raw_database.append([title, [-1. , 2.75, "6.1.1"], [-1. , -1. , "empty"], -1, 2. ]) # ATLAS k/M=1 (6.1.1)
raw_database.append([title, [-1. , 2.15, "6.1.1"], [-1. , -1. , "empty"],  1, 2. ]) # ATLAS k/M=0.5 other BG scaling (6.1.1)
raw_database.append([title, [-1. , 2.95, "6.1.1"], [-1. , -1. , "empty"], -1, 2. ]) # ATLAS k/M=1 other BG scaling (6.1.1)
raw_database.append([title, [ 2. , -1. , "6.1.1"], [-1. , -1. , "empty"], -1, 2. ]) # CMS k/M=0.5, 2.6 sigma (6.1.2)
#spin 1
title="W_{SSM}^\\prime"+arrow+l+"\\nu"
raw_database.append([title, [ 7.7,  7.9, "6.2.6"], [-1. , -1. , "empty"], 12, 1. ]) # ATLAS (6.2.6)
title="W_{SSM}^\\prime"+arrow+"\\tau\\nu      "
raw_database.append([title, [ 6.4,  7. , "6.2.7"], [-1. , -1. , "empty"], 11, 1. ]) # CMS (6.2.7)
title="W_{R}^\\prime"+arrow+" t\\wwbar{b}"+arrow+" b\\wwbar{b}"+l+"\\nu"
raw_database.append([title, [ 4.3,  4.9, "6.2.6"], [-1. , -1. , "empty"], 13, 1. ]) # ATLAS (6.2.6)
title="Z_{SSM}^\\prime"+arrow+"\\tau^{+}\\tau^{-}"
raw_database.append([title, [-1. , -1. , "empty"], [ 6.5,  6.5, "6.2.4"], 10, 1. ]) # HE (6.2.4)
title="Z_{f.a.}^\\prime"+arrow+"\\mu^{+}\\mu^{-}"
raw_database.append([title, [-1  , -1. , "empty"], [ 1. ,  4. , "empty"], -1, 1. ]) # HE f.a. = 1710.06363
title="Z_{SSM}^\\prime"+arrow+l+"^{+}"+l+"^{-}"
raw_database.append([title, [ 6.4, 6.5 , "6.2.5"], [13. , 12.5, "6.2.4"],  9, 1. ]) # ATLAS (6.2.5), HE (6.2.4)
title="Z_{\\psi}^\\prime"+arrow+l+"^{+}"+l+"^{-}"
raw_database.append([title, [ 5.7, 5.8 , "6.2.5"], [-1. , 10. , "6.2.4"],  8, 1. ]) # ATLAS (6.2.5), HE (6.2.4)
title="Z_{SSM}^\\prime"+arrow+" t\\wwbar{t}"
raw_database.append([title, [-1. , -1. , "empty"], [ 6.5,  8.5, "6.4.6"],  6, 1. ]) # HE (6.4.6)
title="Z_{TC2}^\\prime"+arrow+" t\\wwbar{t}"
raw_database.append([title, [-1. ,  4. , "6.2.3"], [ 8. , 10. , "6.4.6"],  5, 1. ]) # ATLAS (6.2.3)
title="G_{RS}"+arrow+" t\\wwbar{t}"
raw_database.append([title, [ 5.7,  6.6, "6.2.2"], [ 9.4, 10.7, "6.2.2"],  4, 1. ]) # CMS (6.2.2)
title="G_{RS}"+arrow+" W^{+}W^{-}"
raw_database.append([title, [-1. , -1. , "empty"], [ 7. ,  8. , "6.4.6"],  3, 1. ]) # HE (6.4.6)
title="HVT"+arrow+" VV"
raw_database.append([title, [ 5.8,  5. , "6.4.4"], [-1. , 11. , "6.4.4"],  2, 1. ]) # ATLAS (6.4.4)
#spin 1/2
title="Q^{*}"+arrow+" jj"
raw_database.append([title, [-1. , -1. , "empty"], [12. , 14. , "6.4.6"], 14, 0.5]) # HE (6.4.6)
title=l+"^{*}"+arrow+l+"\\gamma"
raw_database.append([title, [ 5.1,  5.8, "6.3.1"], [-1. , -1. , "empty"], 18, 0.5]) # CMS (6.3.1)
#title="\\nu^{Heavy}~m_{N}"
#raw_database.append([title, [ 1.6,  3.2, "5.1.1"], [-1. , -1. , "empty"], 16, 0.5])
#title="\\nu^{Heavy}~m_{E}"
#raw_database.append([title, [ 1.8,  3.8, "5.1.1"], [-1. , -1. , "empty"], 17, 0.5])
title="\\nu^{Heavy}~(m_{N}=m_{E})"
raw_database.append([title, [ 1.6,  2. , "5.1.1"], [ 3.2,  3.8, "5.1.1"], 17, 0.5])
title="\\nu^{Majorana}"+arrow+l+" q\\wwbar{q^\\prime}"
raw_database.append([title, [ 7.3,  8. , "5.1.3"], [11.5, 12.5, "5.1.3"], 15, 0.5]) # Lambda=M(N_e) or M(N_mu)
#spin 0
title="H^{++}H^{--}"+arrow+"\\tau_{h}\\,"+l+"^{\\pm}"+l+"^{\\mp}"+l+"^{\\mp}\\,(NH)"
raw_database.append([title, [ -1. ,0.66, "5.1.1"], [-1. , 1.38, "5.1.1"], 22, 0. ])
title="H^{++}H^{--}"+arrow+"\\tau_{h}\\,"+l+"^{\\pm}"+l+"^{\\mp}"+l+"^{\\mp}\\,(IH)"
raw_database.append([title, [ -1. , 0.7, "5.1.1"], [-1. , 1.45, "5.1.1"], 23, 0. ])
title="LQ (pair\\; prod.)"+arrow+" b\\,\\tau"
#raw_database.append([title, [ -1. , 1.5, "5.2.3"], [-1. ,  4. , "5.2.4"], 19, 0. ]) # init David
raw_database.append([title, [ 1.5 ,1.52, "5.2.3"], [ 2.9,  3.4, "5.2.4"], 19, 0. ]) # comments from Patrick Fox
title="LQ"+arrow+" t\\,\\mu"
raw_database.append([title, [ 1.7,  1.9, "5.2.1"], [-1. , -1. , "empty"], 20, 0. ])
title="LQ"+arrow+" t\\,\\tau"
raw_database.append([title, [ 1.2,  1.4, "5.2.1"], [-1. , -1. , "empty"], 21, 0. ])

#raw_database.append(["",   [ , , ], [ , , ], ,])

database=[]
for i in raw_database:
  if i[3]>0 : database.append([i[0], [i[1][1], i[1][0], i[1][2]], [i[2][1], i[2][0], i[2][2]], i[4], i[3]])
database.sort(key=lambda item: item[4], reverse=True)

nAna=len(database)
my_hist=[]
my_hist.append( r.TH1F("limit_HL", "limit_HE", nAna,0.,nAna)) # limit HE
my_hist.append( r.TH1F("limit_HE", "limit_HL", nAna,0.,nAna)) # limit HL
my_hist.append( r.TH1F("disco_HL", "disco_HE", nAna,0.,nAna)) # disco HE
my_hist.append( r.TH1F("disco_HE", "disco_HL", nAna,0.,nAna)) # disco HL

color  = [r.kAzure-9, r.kGreen-9, r.kGreen+3, r.kRed-2]
legend = [
"#splitline{HE-LHC}{#scale[0.75]{#it{#sqrt{s} = 27 TeV}, #it{L = 15 ab^{-1}}}}",
"#splitline{HL-LHC}{#scale[0.75]{#it{#sqrt{s} = 14 TeV}, #it{L = 3 ab^{-1}}}}"
]

process = []
for i in range(nAna): process.append(database[i][0])
val_HL  = []
for i in range(nAna): val_HL.append(database[i][1])
val_HE  = []
for i in range(nAna): val_HE.append(database[i][2])
#
n0=0
n05=0
n1=0
n2=0
spin = []
for i in range(nAna):
  spin_str="-1"
  if database[i][3]==2. :
    spin_str="2"
    n2+=1
  if database[i][3]==1. :
    spin_str="1"
    n1+=1
  if database[i][3]==0.5:
    spin_str="#scale[0.62]{#frac{1}{2}}"
    n05+=1
  if database[i][3]==0. :
    spin_str="0"
    n0+=1
  spin.append(" "+spin_str+" ")

for i_bin in range(nAna):
  my_hist[0].SetBinContent(i_bin+1, val_HE[i_bin][0])
  my_hist[1].SetBinContent(i_bin+1, val_HL[i_bin][0])
  my_hist[2].SetBinContent(i_bin+1, val_HE[i_bin][1])
  my_hist[3].SetBinContent(i_bin+1, val_HL[i_bin][1])
  # empty bin label, handled later in TText
  my_hist[0].GetXaxis().SetBinLabel(i_bin+1," ")

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
  my_hist[3].SetBarWidth(0.5)
  my_hist[3].SetFillStyle(0)
  my_hist[3].SetLineWidth(4)
  my_hist[3].SetLineColor(color[3])
  my_hist[3].SetLineStyle(r.kDotted)

canvas_width=600
if show_section==True: canvas_width=700
canvas = r.TCanvas("test", "test", canvas_width, 600)
canvas.SetTicks(1,1)
canvas.SetLeftMargin(0.27)
if show_section==True: canvas.SetRightMargin(0.09)
else                 : canvas.SetRightMargin(0.02)
r.gStyle.SetOptStat(0)
r.gPad.SetGridx()

x_len=0.25
y_len=0.18
x_low=0.6
y_low=0.11
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

max_factor=1.1
if show_section==True: max_factor=1.5
line2  = r.TLine( -100., n0+n05+n1+n2,  the_max*max_factor, n0+n05+n1+n2  )
line1  = r.TLine( -100., n0+n05+n1-0.1, the_max*max_factor, n0+n05+n1-0.1 )
line05 = r.TLine( -100., n0+n05-0.1,    the_max*max_factor, n0+n05-0.1    )
line0  = r.TLine( -100., n0-0.1,        the_max*max_factor, n0-0.1        )
line2.Draw("same")
line1.Draw("same")
line05.Draw("same")
line0.Draw("same")

Text = r.TLatex()
Text.SetNDC(False)
Text.SetTextAlign(11)

rightText = "95% CL Limit (solid), 5 #sigma Discovery (dash)"
if old_root==True : rightText = "95% CL Limit (solid), 5 #sigma Discovery (hatching)"
Text.SetTextSize(0.035)
Text.DrawLatex(1., nAna+0.3, '#it{' + rightText +'}')

leftText = "#font[22]{Model}"
Text.SetTextSize(0.032)
Text.DrawLatex(-5.7, nAna+0.3, '#it{' + leftText +'}')
leftText = "#font[22]{spin}"
Text.SetTextSize(0.032)
Text.DrawLatex(-0.9, nAna+0.3, '#it{' + leftText +'}')

# labels
label=emu
Text.DrawLatex(-4., -1.5, label)
#
for i_bin in range(nAna):
  str_proc = process[i_bin]
  if show_section==True:
    Text.SetTextSize(0.0265)
    Text.DrawLatex(-6.3, i_bin+0.2, str_proc)
  else:
    Text.SetTextSize(0.0225)
    Text.DrawLatex(-5.8, i_bin+0.2, str_proc)
  str_proc = '#scale[0.9]{'+spin[i_bin]+'}'
  Text.SetTextSize(0.03)
  Text.DrawLatex(-0.6, i_bin+0.2, str_proc)

# write section right tab
if show_section==True:
  str_section = "#font[22]{Section}"
  Text.DrawLatex((the_max*1.1)+0.2, nAna+1., '#it{' + str_section +'}')
  Text.DrawLatex((the_max*1.1)+0.2, nAna+0.3, '#scale[0.58]{#it{#font[22]{HL/HE-LHC}}}')
  for i_bin in range(nAna):
    str_section = ""
    #if val_HL[i_bin][2]!="empty":
    #  str_section+=val_HL[i_bin][2]
    #if val_HE[i_bin][2]!="empty" and val_HE[i_bin][2]!=val_HL[i_bin][2]:
    #  if str_section!="" : str_section+=", "
    #  str_section+=val_HE[i_bin][2]
    if val_HL[i_bin][2]!="empty": str_section+=val_HL[i_bin][2]
    else:                         str_section+="        "
    str_section+="  "
    if val_HE[i_bin][2]!="empty": str_section+=val_HE[i_bin][2]
    else:                         str_section+="     "
    Text.SetTextSize(0.018)
    Text.DrawLatex((the_max*1.1)+0.2, i_bin+0.2, '#it{' + str_section +'}')
  # arxiv
  Text.DrawLatex((the_max*1.1)+0.1, -0.8, '#scale[1.1]{arXiv:}')
  Text.DrawLatex((the_max*1.1)+0.1, -1.4, '#scale[1.1]{1812.07831}')

canvas.RedrawAxis()
canvas.RedrawAxis("g");
canvas.GetFrame().SetBorderSize( 12 )
canvas.Update()
canvas.Modified()

extra=""
if show_section==True: extra="_with_sections"
canvas.Print("summaryLimDisco_HL_HELHC"+extra+".eps")

