#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CmndSvc= for for setting up BPO Crypt. Vault and GPG.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['aasMarmeeManage'], }
csInfo['version'] = '202207112635'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'aasMarmeeManage-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A =CmndSvc= for for setting up Marmee (Multi-Account Resident Mail Exchange Environment) AAS (Accessible Abstract Service).
Manages Mail Account Profiles. Sets up currents. Works with -niche.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = cs.globalContext.get()
# G.icmLibsAppend = __file__
# G.csCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

import sys
import collections

from bisos.marmee import marmeAcctsLib, marmeeCurrentsLib
from bisos.currents import currentsConfig

from bisos.bpo import bpo

#from bisos.icm import clsMethod

from bisos import b

from bisos.crypt import bpoVault


####+BEGIN: b:python:cs:framework/importCmndsModules :cmndsModules ("blee.icmPlayer.bleep" "bisos.bpo.bpo" "bisos.crypt.bpoVault")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_importedCmndsModules~ (blee.icmPlayer.bleep bisos.bpo.bpo bisos.crypt.bpoVault)
#+end_org """

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
    'bisos.bpo.bpo',
    'bisos.crypt.bpoVault',
]

####+END:

####+BEGIN: bx:cs:python:func :funcType "CsFrmWrk" :funcName "g_paramsExtraSpecify" :comment "FmWrk: ArgsSpec"  :retType "Void" :deco "" :argsList "parser"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-CsFrmWrk [[elisp:(outline-show-subtree+toggle)][||]] /g_paramsExtraSpecify/ =FmWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
#+end_org """
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """  #+begin_org
** Module Specific Command Line Parameters. This func is passed to G_main and can not be decorated.
#+end_org """

    G = cs.globalContext.get()
    csParams = cs.CmndParamDict()

    bleep.commonParamsSpecify(csParams)

    bpo.commonParamsSpecify(csParams)

    bpoVault.commonParamsSpecify(csParams)

    cs.argsparseBasedOnCsParams(parser, csParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(csParams)

    return


####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "CmndSvc-s" :extraInfo "class someCommand(cs.Cmnd)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *CmndSvc-s:* |]]  class someCommand(cs.Cmnd)  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

def g_opSysExit(opOutcome):
    print(opOutcome.error)
    sys.exit()

g_outcome = b.op.Outcome()

####+BEGIN: b:python:cs:module/cur_paramsAssign  :curParsList ("usage_bpoId" "vaultName" "vaultPasswd")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Currents   [[elisp:(outline-show-subtree+toggle)][||]] ~cur_examples~ (usage_bpoId vaultName vaultPasswd)
#+end_org """
_parNamesList = [ 'usage_bpoId', 'vaultName', 'vaultPasswd',]
if not (curParsDictValue := currentsConfig.curParsGetAsDictValue_wOp(_parNamesList, outcome=g_outcome).results): g_opSysExit(g_outcome)
cur_usage_bpoId = curParsDictValue['usage_bpoId']
cur_vaultName = curParsDictValue['vaultName']
cur_vaultPasswd = curParsDictValue['vaultPasswd']
def cur_examples():
    cs.examples.execInsert(execLine='bx-currents.cs')
    cs.examples.execInsert(execLine='bx-currents.cs -i usgCursParsGet')
    for each in _parNamesList:
        cs.examples.execInsert(execLine=f'bx-currents.cs -v 20 -i usgCursParsSet {each}={curParsDictValue[each]}')
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :cmndType ""  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<examples>> =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> b.op.Outcome:
        """FrameWrk: ICM Examples"""
####+END:
        self.cmndDocStr(f""" #+begin_org ***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        def cpsInit(): return collections.OrderedDict()
        def menuItem(): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little') # type: ignore
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        logControler = b_io.log.Control()
        logControler.loggerSetLevel(20)

        cs.examples.myName(G.icmMyName(), G.icmMyFullName())

        cs.examples.commonBrief()

        bleep.examples_icmBasic()

        cs.examples.menuChapter('*Currents Examples Settings*')
        cur_examples()

        #  RunBases Examples
        bpoVault.examples_bpo_vault(cur_usage_bpoId, cur_vaultName, cur_vaultPasswd, sectionTitle="default")

####+BEGIN: bx:cs:python:cmnd:subSection :title "marmeAcctsLib Examples"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *withVenv Run PIP Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

        cs.examples.menuChapter('*InMail --- Marmee Svc Access Instance (SAI)*')


        execLineEx("""marmeeSaiInMail.cs""")
        execLineEx("""echo marmeeSaiInMail.cs --bpoId="piu_mbFullUsage" --envRelPath="marmee/gmail/inMail/mohsen.byname"  -i inMailAcctAccessParsSet userName="UserName" userPasswd="UserPasswd" imapServer="IMAPServer" """)

        b.niche.examplesNicheRun("usageEnvs")

        return(cmndOutcome)



####+BEGIN: b:python:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_paramsExtraSpecify" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_icmMain~ (csInfo, _examples_, g_paramsExtraSpecify, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
