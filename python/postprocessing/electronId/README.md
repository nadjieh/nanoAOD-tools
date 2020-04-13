Based on central nanoAODv6 with the content described [here](https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/data101X_doc.html)
# Electron and their properties to keep
+ isPFCand and Kinematics: eta, phi, and pt.
+ MC truth info: Electron_genPartFlav, Electron_genPartIdx
+ Electrons must have the latest loose identification criteria.
   + **Fall17 v2** from [EGM twiki](https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Cut_Based_Electron_ID_for_Run_2) and the code [here](https://github.com/cms-egamma/ggAnalysis/blob/102X-egpos2019/ggNtuplizer/plugins/ggNtuplizer_electrons.cc#L630-L655). 
   + It corresponds to **Electron_cutBased == 2** in nanoAOD
   + Store Electron_mvaFall17V1Iso and V2
+ The information on all impact parameters and their error
   + dxy (Err), dz (Err) in nanoAOD
   + Electron_ip3d, Electron_sip3d
+ Nearest Jet info
   + Electron_jetIdx
   + Electron_jetRelIso
+ Photon Info
   + Electron_photonIdx
+ Isolation variables
   + Electron_jetRelIso
   + Electron_miniPFRelIso_all
   + Electron_miniPFRelIso_chg
   + Electron_pfRelIso03_all
   + Electron_pfRelIso03_chg
+ Additional interesting variables
   + Electron_eInvMinusPInv
   + Electron_energyErr
   + TTH Id value
   + Electron_lostHits
# Jets and their properties
+ Kinematics (pt, eta, phi)
+ Jet_puId
+ Jet_qgl
+ Jet_rawFactor
+ B-tagging info
   + Jet_btagCSVV2, Jet_btagDeepB, Jet_btagDeepC, Jet_btagDeepFlavB
# Gen Particle collection
+ GenPart
