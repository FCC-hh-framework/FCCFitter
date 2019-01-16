import ROOT as r

axis = "X"
#axis = "Y"
# -> Y is not working yet, follow the ROOT talk :
# https://root-forum.cern.ch/t/draw-y-axis-histograms-hbar-option-not-satisfying/32307/5

database=[]

# ana, 27 TeV, 15 ab-1 , [disco, limit]
database.append(["Z\'_{SSM} #rightarrow #tau^{+}#tau^{-}", [ 6., 6.]])
#database.append(["Z\'_{f.a.} #rightarrow #mu^{+}#mu^{-}",  [ 1., 4.]]) # f.a. = 1710.06363
database.append(["Z\'_{SSM} #rightarrow l^{+}l^{-}",       [13.,13.]])
database.append(["G_{RS} #rightarrow W^{+}W^{-}",          [ 7., 8.]])  
database.append(["Z\'_{SSM} #rightarrow t#bar{t}",         [ 6., 8.]])
database.append(["Z\'_{TC2} #rightarrow t#bar{t}",         [ 8.,10.]])
database.append(["Q* #rightarrow jj",                      [12.,14.]])
database.append(["ATLAS, HL-LHC",                          [25.,10.]])
database.append(["extra2",                                 [ 5., 8.]])
database.append(["extra3",                                 [15.,20.]])
database.append(["extra4",                                 [20.,12.]])

nAna=len(database)
nbins = (2*nAna)
h_27=[]
h_27.append( r.TH1D("h_27_1", "h_27_1", nbins,0.,nbins))
h_27.append( r.TH1D("h_27_2", "h_27_2", nbins,0.,nbins))

nMax=len(h_27)-1

color  = [r.kAzure-9, r.kRed+1]
legend = ["5 #sigma Disco", "95% CL"]

process = []
for i in range(nAna): process.append(database[i][0])
val27   = []
for i in range(nAna): val27.append(database[i][1])

count_ana = 0
for i_bin in xrange( 1, nbins+1 ):
  if i_bin%2==0: continue
  for i in xrange( 0, nMax+1 ) : h_27[i].SetBinContent(i_bin, val27[count_ana][i])
  str_proc = '#scale[1.02]{#font[22]{'+process[count_ana]+'}}'
  h_27[0].GetXaxis().SetBinLabel(i_bin,str_proc)
  #if axis=="X": h_27[0].GetXaxis().ChangeLabel(i_bin,-60.,-1.,-1,-1,-1,str_proc)
  count_ana+=1

h_27[0].SetLineColorAlpha(color[0],0.)
h_27[0].SetFillColorAlpha(color[0],0.8)
h_27[0].SetMarkerColorAlpha(color[0],0.)
h_27[1].SetLineColor(color[1])
h_27[1].SetLineWidth(3)
h_27[1].SetLineStyle(2)

canvas = r.TCanvas("test", "test", 600, 600)
canvas.SetTicks(1,1)
if axis=="Y":
  canvas.SetLeftMargin(0.21)
  canvas.SetRightMargin(0.02)
r.gStyle.SetOptStat(0)
if axis=="Y": r.gPad.SetGridx()
if axis=="X": r.gPad.SetGridy()

leg_x=[0.67,0.72,0.92,0.90]
leg_y=[0.73,0.52,0.98,0.70]
leg_coor=[]
if axis=="X":
  for i in range(len(leg_x)): leg_coor.append(leg_x[i])
if axis=="Y":
  for i in range(len(leg_y)): leg_coor.append(leg_y[i])

leg = r.TLegend(leg_coor[0],leg_coor[1],leg_coor[2],leg_coor[3])
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetLineColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.035)
leg.SetTextFont(42)

the_max=max(h_27[0].GetMaximum(),h_27[1].GetMaximum())
h_27[0].SetMaximum(the_max*1.1)
h_27[0].SetTitle("")
h_27[0].GetYaxis().SetTitleOffset(1.30)
h_27[0].GetYaxis().SetTitle("Mass scale [TeV]")
h_27[0].GetXaxis().SetLabelSize(0.05)
h_27[0].GetXaxis().SetTickLength(0.)

if axis=="X":
  h_27[0].Draw()
  h_27[1].Draw("same")
if axis=="Y": 
  h_27[0].Draw("hbar")
  h_27[1].Draw("hbarsame")

for i in xrange( 0, nMax+1 ) :
  leg.AddEntry(h_27[i],legend[i])
leg.Draw("same")

Text = r.TLatex()
Text.SetNDC()

leftText27      = "HE-LHC Simulation (Delphes), #sqrt{s} = 27 TeV, 15 ab^{-1}"
Text.SetTextAlign(31);
Text.SetTextSize(0.04)
if axis=="X": Text.DrawLatex(0.92, 0.92, '#it{' + leftText27     +'}')
if axis=="Y": Text.DrawLatex(0.97, 0.92, '#it{' + leftText27     +'}')

canvas.RedrawAxis()
canvas.RedrawAxis("g");
canvas.GetFrame().SetBorderSize( 12 )
canvas.Modified()
canvas.Update()

extra="_onlyHELHC_15"
canvas.Print("summaryDisco"+extra+".pdf")

