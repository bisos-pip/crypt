# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CS-Lib= for creating and managing BPO's gpg and encryption/decryption.
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
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bpoGpg'], }
icmInfo['version'] = '202208073306'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'bpoGpg-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos.crypt/_nodeBase_/fullUsagePanel-en.org][PyFwrk bisos.crypt Panel]]
Module description comes here.
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

####+BEGIN: bx:icm:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

import os
# import pwd
# import grp
# import collections
# import enum
#

#import traceback

import collections

import pathlib

# from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

# from bisos.basics import pattern

from bisos.bpo import bpo
#from bisos.pals import palsSis
#from bisos.icm import fpath

from bisos import bpf

import gnupg

#import logging

#import shutil

import pykeepass_cache
import pykeepass

####+BEGIN: bx:dblock:python:class :className "BpoGpg" :superClass "object" :comment "Run Bases of a Bpo" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BpoGpg/ object =Run Bases of a Bpo=  [[elisp:(org-cycle)][| ]]
#+end_org """
class BpoGpg(object):
####+END:
    """
** Abstraction of the Gpgs of BPOs (ByStar Portable Object)
"""
####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            bpoId,
    ):
        self.bpoId = bpoId
        self.bpo = bpo.EffectiveBpos.givenBpoIdObtainBpo(bpoId, bpo.Bpo)

####+BEGIN: bx:icm:py3:method :methodName "repoBasePath_obtain" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /repoBasePath_obtain/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def repoBasePath_obtain(
####+END:
            self,
    ) -> pathlib.Path:
        """ #+begin_org
*** TODO [[elisp:(org-cycle)][| *MethodDesc:* | ]] Rename vault, vaults ---  Confirm that ~bpoGpgsBaseDir~ exists and return that.
        #+end_org """

        bpoGpgsBaseDir = pathlib.Path(
            os.path.join(
                self.bpo.bpoBaseDir,
                'gpgKeys',
            )
        )
        if not os.path.isdir(bpoGpgsBaseDir):
            bpoGpgsBaseDir.mkdir(parents=True, exist_ok=True)

        return bpoGpgsBaseDir

####+BEGIN: bx:icm:py3:method :methodName "keysFilePath_obtain" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /keysFilePath_obtain/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def keysFilePath_obtain(
####+END:
            self,
            gpgBaseName,
    ) -> pathlib.Path:
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Based on =vault= create BPO's {vault}.kdbx. Return that path.
        #+end_org """

        repoBase = self.repoBasePath_obtain()

        gpgBaseDir = pathlib.Path(
            os.path.join(
                repoBase,
                gpgBaseName,
            )
        )

        if not os.path.isdir(gpgBaseDir):
            gpgBaseDir.mkdir(parents=True, exist_ok=True)

        return gpgBaseDir


####+BEGIN: bx:icm:py3:method :methodName "genKey" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /genKey/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def genKey(
####+END:
            self,
            gpgFileName,
            nameEmail,
            passphrase,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Generate Key.
        #+end_org """
        keysBaseDir = self.keysFilePath_obtain(gpgFileName,)

        gpg = gnupg.GPG(gnupghome=keysBaseDir)
        # generate key
        input_data = gpg.gen_key_input(
            name_email=nameEmail,
            passphrase=passphrase,
        )
        key = gpg.gen_key(input_data)
        print(key)



####+BEGIN: bx:icm:py3:method :methodName "encryptStr" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /encryptStr/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def encryptStr(
####+END:
            self,
            vault,
            passwd,
    ):
    # ) -> typing.Optional[pykeepass.PyKeePass]:
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Open the vault and return a kp. vault must exist. passwd is mandatory.
        Thereafter, for a while actions can be performed without the password.
*** TODO Add passhole to panel.
        #+end_org """

        vaultFilePath = self.vaultFilePath_obtain(vault)

        if not os.path.exists(vaultFilePath):
            icm.EH_problem_usageError(f"""Missing vault={vaultFilePath}""")
            return typing.cast(pykeepass.PyKeePass, None)

        if not passwd:
            icm.EH_problem_usageError(f"""Missing passwd""")
            return typing.cast(pykeepass.PyKeePass, None)

        #kp = pykeepass_cache.PyKeePass(vaultFilePath, passwd, timeout=1000)
        kp = pykeepass_cache.PyKeePass(vaultFilePath, passwd)

        return typing.cast(pykeepass.PyKeePass, kp)

####+BEGIN: bx:icm:py3:method :methodName "vaultClose" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultClose/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultClose(
####+END:
            self,
            vault,
            passwd,
    ):
        """ #+begin_org
*** TODO [[elisp:(org-cycle)][| *MethodDesc:* | ]]  UnImplemented. Close the vault.
        #+end_org """

        return vault, passwd


####+BEGIN: bx:icm:py3:section :title "Common Parameters Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-ParSpec  [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    icmParams,
):
####+END:
    icmParams.parDictAdd(
        parName='vault',
        parDescription="Gpg Name -- uniq within bpo/vault",
        parDataType=None,
        parDefault='fpGpg',
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--vault',
    )
    icmParams.parDictAdd(
        parName='passwd',
        parDescription="Password (General Purpose)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--passwd',
    )

####+BEGIN: bx:icm:py3:section :title "CS-Lib Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Lib Examples*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:dblock:python:func :funcName "examples_bpo_gpg" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList "oneBpo vault passwd sectionTitle=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-examples [[elisp:(outline-show-subtree+toggle)][||]] /examples_bpo_gpg/ =Show/Verify/Update For relevant PBDs= retType=none argsList=(oneBpo vault passwd sectionTitle=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_bpo_gpg(
    oneBpo,
    vault,
    passwd,
    sectionTitle=None,
):
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    # def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    if sectionTitle == "default":
        icm.cmndExampleMenuChapter('*Manage BPO Gpg*')

    if not oneBpo:
        return

    icm.cmndExampleMenuChapter('*Primary Commands*')

    cmndName = "vaultCreate"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "vaultOpen"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "vaultClose"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "vaultGroupAdd"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "vaultEntryUpdate"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "vaultEntryRead"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')


    cmndName = "vaultEntryDelete"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')


    icm.cmndExampleMenuChapter('*Secondary Commands*')

    cmndName = "bpoGpgPrep"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "bpoGpgList"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:icm:py3:section :title "Primary Command Services"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Primary Command Services*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gpg_genKey" :comment "" :parsMand "bpoId" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<gpg_genKey>> parsMand=bpoId parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class gpg_genKey(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        # if bpf.subProc.WOpW(invedBy=self,).bash(
        #         f"""gpg --generate-key""",
        # ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        thisBpo = BpoGpg(bpoId,)

        thisBpo.genKey('bisos', 'bisos@example.com' , 'passphrase')


        return cmndOutcome


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pyEncrypt" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<pyEncrypt>> parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class pyEncrypt(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        gpg = gnupg.GPG()   # gpg = gnupg.GPG(gnupghome="/home/sammy/.gnupg")
        #home_fs = fs.open_fs(".")

        cmndArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, effectiveArgsList)

        for each in cmndArgs:
            with open(each, "rb") as f:

                status = gpg.encrypt_file(
                    f,
                    recipients=["mohsen.byname@gmail.com"],
                    output= f"{each}.gpg"
                )
                print("ok: ", status.ok)
                print("status: ", status.status)
                print("stderr: ", status.stderr)

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """  #+begin_org
** [[elisp:(org-cycle)][| *cmndArgsSpec:* | ]]
        #+end_org """
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cmndArgs",
            argChoices=[],
            argDescription="List Of CmndArgs To Be Processed. Each As Any."
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pySymEncrypt" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<pySymEncrypt>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class pySymEncrypt(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        gpg = gnupg.GPG()
        data = 'the quick brown fow jumps over the laxy dog.'
        passphrase='12345'
        crypt = gpg.encrypt(
            data,
            recipients=None,
            symmetric='AES256',
            passphrase=passphrase,
            armor=False,
        )
        print(crypt.data)

        clear = gpg.decrypt(
            crypt.data,
            passphrase=passphrase,
        )

        print(clear)

        return cmndOutcome



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:


####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
