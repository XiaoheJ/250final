import glob
import ROOT
import os
import math
import argparse
import sys
from ROOT import *
import xAODRootAccess.GenerateDVIterators

ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasLabels.C");
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(0)

signal_regions = {"SR0": ""}

for sr in signal_regions:

    files100_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399030.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p01ns.072418_VeryLooseLLH_trees.root/*.root")
    t100_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_0: t100_0.Add(f)

    files100_0_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399030.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p01ns.072418_noD0LLH_trees.root/*.root")
    t100_0_ = ROOT.TChain("trees_SR_highd0_")
    for f in files100_0_: t100_0_.Add(f)

    files100_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399031.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p1ns.072418_VeryLooseLLH_trees.root/*.root")
    t100_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_1: t100_1.Add(f)

    files100_1_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399031.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p1ns.072418_noD0LLH_trees.root/*.root")
    t100_1_ = ROOT.TChain("trees_SR_highd0_")
    for f in files100_1_: t100_1_.Add(f)

    files500_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399046.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p01ns.072418_VeryLooseLLH_trees.root/*.root")
    t500_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files500_0: t500_0.Add(f)

    files500_0_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399046.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p01ns.072418_noD0LLH_trees.root/*.root")
    t500_0_ = ROOT.TChain("trees_SR_highd0_")
    for f in files500_0_: t500_0_.Add(f)

    files500_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399047.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p1ns.072418_VeryLooseLLH_trees.root/*.root")
    t500_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files500_1: t500_1.Add(f)

    files500_1_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399047.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p1ns.072418_noD0LLH_trees.root/*.root")
    t500_1_ = ROOT.TChain("trees_SR_highd0_")
    for f in files500_1_: t500_1_.Add(f)

    files700_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399054.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p01ns.072418_VeryLooseLLH_trees.root/*.root")
    t700_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files700_0: t700_0.Add(f)

    files700_0_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399054.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p01ns.072418_noD0LLH_trees.root/*.root")
    t700_0_ = ROOT.TChain("trees_SR_highd0_")
    for f in files700_0_: t700_0_.Add(f)

    files700_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399055.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p1ns.072418_VeryLooseLLH_trees.root/*.root")
    t700_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files700_1: t700_1.Add(f)

    files700_1_ = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399055.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p1ns.072418_noD0LLH_trees.root/*.root")
    t700_1_ = ROOT.TChain("trees_SR_highd0_")
    for f in files700_1_: t700_1_.Add(f)

    files500_1lrt = glob.glob("/eos/user/l/lhoryn/highd0/testDAODRPVLL/out.FTNTUP.SlepSlep_directLLP.500_0p1ns.DAODRPVLL.standardveryloose.root")
    t500_1lrt = ROOT.TChain("trees_SR_highd0_")
    for f in files500_1lrt: t500_1lrt.Add(f)

    files500_1lrt_ = glob.glob("/eos/user/l/lhoryn/highd0/testDAODRPVLL/out.FTNTUP.SlepSlep_directLLP.500_0p1ns.DAODRPVLL.nod0veryloose.root")
    t500_1lrt_ = ROOT.TChain("trees_SR_highd0_")
    for f in files500_1lrt_: t500_1lrt_.Add(f)

    files500_0noph_ = glob.glob("/afs/cern.ch/user/x/xjia/all/user.lhoryn.mc16_13TeV.399046.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p01ns.080319_3_trees.root/*.root")
    t500_0noph_ = ROOT.TChain("trees_SR_highd0_")
    for f in files500_0noph_: t500_0noph_.Add(f)

    h2 = ROOT.TH1F("2","2",15,0,30)
    h2_ = ROOT.TH1F("2_","2_",15,0,30)

    f1 = ROOT.TFile("num1.root")
    num = f1.Get("num")

    f1_ = ROOT.TFile("den1.root")
    den = f1_.Get("den")

    heff2 = ROOT.TEfficiency(num,den)

    for event in t500_0noph_:

        for i in xrange(len(event.truthLepton_d0)):
            
            if abs(event.truthLepton_pdgId[i]) == 11 and abs(event.truthLepton_eta[i]) < 2.47 and event.truthLepton_pt[i] > 50:

                h2_.Fill(event.truthLepton_d0[i])

        for i in xrange(len(event.electron_truthMatchedBarcode)):

            barcode = event.electron_truthMatchedBarcode[i]
            found_match = False
            true_d0 = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j]) < 2.47 and event.truthLepton_pt[j] > 50:
                                
                        found_match = True
                        true_d0 = event.truthLepton_d0[j]
                        break
                    
            if not found_match: continue
            
            h2.Fill(true_d0)

    heff1 = ROOT.TEfficiency(h2,h2_)

    heff1.SetTitle("Efficiency vs Truth d0; truth d0 [mm]; efficiency")
    heff1.SetMarkerColor(ROOT.kBlue)
    heff2.SetMarkerColor(ROOT.kRed)
    
    c = ROOT.TCanvas()
    heff1.Draw("AP")
    heff2.Draw("SAME")

    leg = ROOT.TLegend(.2,.2,.4,.3)
    leg.AddEntry(heff1, "with ident", "lep")
    leg.AddEntry(heff2, "without ident", "lep")
    leg.Draw("same")

    ROOT.gPad.Update()
    graph = heff1.GetPaintedGraph()
    graph.SetMinimum(0)
    graph.SetMaximum(1)
    ROOT.gPad.Update()
    c.Update()
    c.SaveAs("eff.pdf")

    raw_input("...")
