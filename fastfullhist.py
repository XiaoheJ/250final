import glob
import ROOT
import os
import math
import argparse
import sys
from ROOT import *

ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasLabels.C");
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(0)

signal_regions = {"SR0": ""}

for sr in signal_regions:

    files_af2 = glob.glob("/eos/user/l/lhoryn/highd0/111918/user.lhoryn.mc16_13TeV.399039.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_300_0_0p1ns.111818_xj_af2_trees.root/*.root")
    t_af2 = ROOT.TChain("trees_SR_highd0_")
    for f in files_af2: t_af2.Add(f)

    files_full = glob.glob("/eos/user/l/lhoryn/highd0/111918/user.lhoryn.mc16_13TeV.399039.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_300_0_0p1ns.111818_xj_full_trees.root/*.root")
    t_full = ROOT.TChain("trees_SR_highd0_")
    for f in files_full: t_full.Add(f)

    h1 = ROOT.TH1F("1","1",90,0,30)
    h2 = ROOT.TH1F("2","2",90,0,30)

    for event in t_af2:

        for i in xrange(len(event.truthLepton_d0)):
            
            if abs(event.truthLepton_pdgId[i]) == 13 and abs(event.truthLepton_eta[i]) < 2.47 and event.truthLepton_pt[i] > 50:

                h1.Fill(event.truthLepton_d0[i])

    for event in t_full:

        for i in xrange(len(event.truthLepton_d0)):
            
            if abs(event.truthLepton_pdgId[i]) == 13 and abs(event.truthLepton_eta[i]) < 2.47 and event.truthLepton_pt[i] > 50:

                h2.Fill(event.truthLepton_d0[i])

    n1 = h1.GetEntries()
    h1.Scale(1/n1)
    n2 = h2.GetEntries()
    h2.Scale(1/n2)

    h1.SetTitle("Efficiency vs Truth d0; truth d0 [mm]; percent")
    h1.SetLineColor(ROOT.kBlue)
    h2.SetLineColor(ROOT.kRed)
    h1.GetXaxis.SetMaximum(5)
    c = ROOT.TCanvas()
    h1.Draw("hist")
    h2.Draw("hist same")

    leg = ROOT.TLegend(.2,.2,.4,.3)
    leg.AddEntry(h1, "af2", "l")
    leg.AddEntry(h2, "full", "l")
    leg.Draw("same")

    raw_input("...")
