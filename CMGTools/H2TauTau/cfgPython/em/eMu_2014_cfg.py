import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.config import printComps

# import all analysers:
# Heppy analyzers
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer               import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.EventSelector              import EventSelector
# from PhysicsTools.Heppy.analyzers.examples.TriggerAnalyzer        import TriggerAnalyzer
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer          import VertexAnalyzer
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer             import PileUpAnalyzer
from PhysicsTools.Heppy.analyzers.gen.GeneratorAnalyzer           import GeneratorAnalyzer

# Tau-tau analyzers
from CMGTools.H2TauTau.proto.analyzers.JetAnalyzer                import JetAnalyzer
from CMGTools.H2TauTau.proto.analyzers.EmbedWeighter              import EmbedWeighter
from CMGTools.H2TauTau.proto.analyzers.GenErsatzAnalyzer          import GenErsatzAnalyzer
from CMGTools.H2TauTau.proto.analyzers.EMuAnalyzer                import EMuAnalyzer
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerEMu    import H2TauTauTreeProducerEMu
from CMGTools.H2TauTau.proto.analyzers.DYJetsFakeAnalyzer         import DYJetsFakeAnalyzer
from CMGTools.H2TauTau.proto.analyzers.WNJetsAnalyzer             import WNJetsAnalyzer
from CMGTools.H2TauTau.proto.analyzers.NJetsAnalyzer              import NJetsAnalyzer
from CMGTools.H2TauTau.proto.analyzers.HiggsPtWeighter            import HiggsPtWeighter
from CMGTools.H2TauTau.proto.analyzers.WNJetsTreeAnalyzer         import WNJetsTreeAnalyzer
from CMGTools.H2TauTau.proto.analyzers.LeptonWeighter             import LeptonWeighter

from CMGTools.RootTools.analyzers.VBFSimpleAnalyzer               import VBFSimpleAnalyzer
from CMGTools.H2TauTau.triggerMap                                 import pathsAndFilters

puFileMC   = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/MC_Summer12_PU_S10-600bins.root'
puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/Data_Pileup_2012_ReRecoPixel-600bins.root' ## new for rereco Pixel Lumi 17/9/2013

eventSelector = cfg.Analyzer(
  EventSelector  ,
  'EventSelector',
  toSelect = [
  ]
  )

jsonAna = cfg.Analyzer(
  JSONAnalyzer         ,
  name = 'JSONAnalyzer',
  )

# triggerAna = cfg.Analyzer(
#   TriggerAnalyzer  ,
#   'TriggerAnalyzer',
#   verbose = False
#   )

vertexAna = cfg.Analyzer(
  VertexAnalyzer                         ,
  'VertexAnalyzer'                       ,
  goodVertices = 'offlinePrimaryVertices', 
  fixedWeight  = 1                       ,
  verbose      = False
  )

pileUpAna = cfg.Analyzer(
  PileUpAnalyzer  ,
  'PileUpAnalyzer',
  true = True
  )

genAna = GeneratorAnalyzer.defaultConfig
    
EMuAna = cfg.Analyzer(
  MuEleAnalyzer                ,
  'MuEleAnalyzer'              ,
  pt1        = 10.             ,
  eta1       = 2.5             ,
  iso1       = 10.             ,
  looseiso1  = 10.             ,
  pt2        = 10.             ,
  eta2       = 2.5             ,
  iso2       = 10.             ,
  looseiso2  = 10.             ,
  m_min      = 10              ,
  m_max      = 99999           ,
  dR_min     = 0.5             ,
  triggerMap = pathsAndFilters ,
  jetPt      = 30.             ,    
  jetEta     = 4.7             ,
  relaxJetId = False           ,
  verbose    = False           
  )

dyJetsFakeAna = cfg.Analyzer(
  DYJetsFakeAnalyzer  ,
  'DYJetsFakeAnalyzer',
  channel = 'em'      ,
  )

jetAna = cfg.Analyzer(
  JetAnalyzer                 ,
  'JetAnalyzer'               ,
  jetCol      = 'slimmedJets' , # <- These are CHS jets
  #jetCol      = 'patJetsAK4PF', # <- These are plain PF jets
  jetPt       = 20.           ,
  jetEta      = 4.7           ,
  btagSFseed  = 123456        ,
  relaxJetId  = False         , 
  jerCorr     = False         ,
  #jesCorr     = 1.            ,
  puJetIDDisc = 'pileupJetIdFull:full53xDiscriminant',
  )

# defined for vbfAna and eventSorter
vbfKwargs = dict( Mjj = 500, deltaEta = 3.5 )

vbfAna = cfg.Analyzer(
  VBFSimpleAnalyzer            ,
  'VBFSimpleAnalyzer'          ,
#   vbfMvaWeights = os.environ['CMSSW_BASE'] + '/src/CMGTools/H2TauTau/data/VBFMVA_BDTG_HCP_52X.weights.xml',
#   jetCol        = 'cmgPFJetSel',
  jetPt         = 30.          ,
  looseJetPt    = 20           ,
  jetEta        = 4.7          ,
  cjvPtCut      = 30.          ,
  btagSFseed    = 123456       ,
  relaxJetId    = False        ,
  **vbfKwargs                  
  )

embedWeighter = cfg.Analyzer(
  EmbedWeighter            ,
  name     ='EmbedWeighter',
  isRecHit = False         ,
  verbose  = False
  )

NJetsAna = cfg.Analyzer(
  NJetsAnalyzer   ,
  'NJetsAnalyzer' ,
  fillTree = True ,
  verbose  = False
  )

muonWeighter = cfg.Analyzer(
  LeptonWeighter       ,
  'LeptonWeighterMuon',
  effWeight   = None   ,
  effWeightMC = None   ,
  lepton      = 'leg1' ,
  verbose     = False  ,
  disable     = True   ,
  )

eleWeighter = cfg.Analyzer(
  LeptonWeighter       ,
  'LeptonWeighterEle'  ,
  effWeight   = None   ,
  effWeightMC = None   ,
  lepton      = 'leg2' ,
  verbose     = False  ,
  disable     = True   ,
  )

higgsWeighter = cfg.Analyzer(
    HiggsPtWeighter,
    'HiggsPtWeighter',
    )

treeProducer = cfg.Analyzer(
  H2TauTauTreeProducerMuEle  ,
  'H2TauTauTreeProducerMuEle',
  )

###################################################
### CONNECT SAMPLES TO THEIR ALIASES AND FILES  ###
###################################################
from CMGTools.H2TauTau.proto.samples.phys14.diTau_Ric_Jan27 import *

###################################################
###     ASSIGN JET SMEAR, SCALE and PU to MC    ###
###################################################
mc_jet_scale = 1.
mc_jet_smear = 0.
for mc in MC_list:
  mc.jetScale   = mc_jet_scale
  mc.jetSmear   = mc_jet_smear
  mc.puFileData = puFileData
  mc.puFileMC   = puFileMC

selectedComponents = allsamples

###################################################
###             SET COMPONENTS BY HAND          ###
###################################################

# selectedComponents  = [ ZZJetsTo4L ]
# for c in selectedComponents : c.splitFactor *= 5

###################################################
###                  SEQUENCE                   ###
###################################################
sequence = cfg.Sequence( [
  #eventSelector       ,
  jsonAna             ,
  #triggerAna          ,
  vertexAna           ,
  EMuAna              ,
  genAna              ,
  dyJetsFakeAna       ,
  jetAna              ,
  vbfAna              ,
  pileUpAna           ,
  embedWeighter       ,
  NJetsAna            ,
  muonWeighter        , 
  eleWeighter         ,
  higgsWeighter       ,
  treeProducer        ,
  ] )

###################################################
###    SET THE TRIGGERS TO BE USED WITH DATA    ###
###################################################
# for data in data_parked_2012:
#   data.triggers  = data_parked_triggers_2012  ## ORDER MATTERS!
#   data.triggers += data_triggers_2012         ## ORDER MATTERS!
  
###################################################
###     SET THE TRIGGERS TO BE USED WITH MC     ###
###################################################
# for mc in MC_list:
#   mc.triggers = ['HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6']

###################################################
###   SET THE TRIGGERS TO BE USED WITH RH EMB   ###
###################################################
# for emb in embed_list:
#   emb.triggers = emb_rechit_triggers

###################################################
###            SET BATCH OR LOCAL               ###
###################################################
test = 1 # test = 0 run on batch, test = 1 run locally
if test == 1 :
  cache              = True
  comp               = HiggsGGH125
  comp.triggers      = [] # empty for now
  selectedComponents = [comp]
  comp.splitFactor   = 1
  comp.files         = comp.files[:1]

###################################################
###                SOME PRINTOUT                ###
###################################################
print '_'*70
print 'Processing...' 
print [s.name for s in selectedComponents]

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components   = selectedComponents,
                     sequence     = sequence          ,
                     services     = []                ,  
                     events_class = Events
                     )
