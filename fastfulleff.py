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

    h1 = ROOT.TH1F("1","1",15,-0.15,0.15)
    h1_ = ROOT.TH1F("1_","1_",15,-0.15,0.15)
    h2 = ROOT.TH1F("2","2",15,-0.15,0.15)
    h2_ = ROOT.TH1F("2_","2_",15,-0.15,0.15)

    for event in t_af2:

        for i in xrange(len(event.truthLepton_d0)):
            
            if abs(event.truthLepton_pdgId[i]) == 13 and abs(event.truthLepton_eta[i]) < 2.47 and event.truthLepton_pt[i] > 50:

                h1_.Fill(event.truthLepton_eta[i])

        for i in xrange(len(event.muon_truthMatchedBarcode)):

            barcode = event.muon_truthMatchedBarcode[i]
            found_match = False
            true = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j]) < 2.47 and event.truthLepton_pt[j] > 50:
                                
                        found_match = True
                        true = event.truthLepton_eta[j]
                        break
                    
            if not found_match: continue
            
            h1.Fill(true)

    heff1 = ROOT.TEfficiency(h1,h1_)

    for event in t_full:

        for i in xrange(len(event.truthLepton_d0)):
            
            if abs(event.truthLepton_pdgId[i]) == 13 and abs(event.truthLepton_eta[i]) < 2.47 and event.truthLepton_pt[i] > 50:

                h2_.Fill(event.truthLepton_eta[i])

        for i in xrange(len(event.muon_truthMatchedBarcode)):

            barcode = event.muon_truthMatchedBarcode[i]
            found_match = False
            true = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j]) < 2.47 and event.truthLepton_pt[j] > 50:
                                
                        found_match = True
                        true = event.truthLepton_eta[j]
                        break
                    
            if not found_match: continue
            
            h2.Fill(true)

    heff2 = ROOT.TEfficiency(h2,h2_)

    heff1.SetTitle("Efficiency vs Truth Eta; truth eta; efficiency")
    heff1.SetMarkerColor(ROOT.kBlue)
    heff2.SetMarkerColor(ROOT.kRed)
    
    c = ROOT.TCanvas()
    heff1.Draw("AP")
    heff2.Draw("SAME")

    leg = ROOT.TLegend(.2,.2,.4,.3)
    leg.AddEntry(heff1, "af2", "lep")
    leg.AddEntry(heff2, "full", "lep")
    leg.Draw("same")

    ROOT.gPad.Update()
    graph = heff1.GetPaintedGraph()
    graph.SetMinimum(0)
    graph.SetMaximum(1)
    ROOT.gPad.Update()
    c.Update()

    raw_input("...")
