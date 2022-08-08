# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CS-Lib= for creating and managing BPO's vaults.
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
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bpoVault'], }
icmInfo['version'] = '202207155149'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'bpoVault-Panel.org'
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

#import logging

#import shutil

import pykeepass_cache
import pykeepass

####+BEGIN: bx:dblock:python:class :className "BpoVault" :superClass "object" :comment "Run Bases of a Bpo" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic [[elisp:(outline-show-subtree+toggle)][||]] /BpoVault/ object =Run Bases of a Bpo=  [[elisp:(org-cycle)][| ]]
#+end_org """
class BpoVault(object):
####+END:
    """
** Abstraction of the Vaults of BPOs (ByStar Portable Object)
"""
####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
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
*** TODO [[elisp:(org-cycle)][| *MethodDesc:* | ]] Rename vault, vaults ---  Confirm that ~bpoVaultsBaseDir~ exists and return that.
        #+end_org """

        bpoVaultsBaseDir = pathlib.Path(
            os.path.join(
                self.bpo.bpoBaseDir,
                'vault',
            )
        )
        if not os.path.exists(bpoVaultsBaseDir):
            bpoVaultsBaseDir.mkdir(parents=True, exist_ok=True)

        return bpoVaultsBaseDir

####+BEGIN: bx:icm:py3:method :methodName "vaultFilePath_obtain" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultFilePath_obtain/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultFilePath_obtain(
####+END:
            self,
            vault,
    ) -> pathlib.Path:
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Based on =vault= create BPO's {vault}.kdbx. Return that path.
        #+end_org """

        vaultFileName = f"{vault}.kdbx"
        repoBase = self.repoBasePath_obtain()

        return (
            pathlib.Path(
                os.path.join(
                    repoBase,
                    vaultFileName,
                )
            )
        )


####+BEGIN: bx:icm:py3:method :methodName "vaultCreate_wOp" :methodType "wOp" :retType "OpOutcome" :deco "default" :argsList "typed"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-wOp    :: /vaultCreate_wOp/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultCreate_wOp(
####+END:
            self,
            vault,
            passwd,
            outcome: typing.Optional[bpf.op.Outcome] = None,
    ) -> bpf.op.Outcome:
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Create an empty database if it does not exist. Implemented with ph (passhole) as a command.
*** TODO dependence on ph is un-necessary. relevant part of passhole should be merged with pykeepass.
        #+end_org """

        if not outcome:
           outcome = bpf.op.Outcome()

        vaultFilePath = self.vaultFilePath_obtain(vault)

        if os.path.exists(vaultFilePath):
            icm.ANN_write(f"""{vaultFilePath} Exists. Creation Skipped""")
            return outcome
        else:
            icm.ANN_write(f"No database file found at {vaultFilePath}")
            icm.ANN_write("Creating it...")

        # DEBUG -- invkedBy=outcome
        if bpf.subProc.WOpW(log=1).bash(
                f"""ph init --name {vault} --database {vaultFilePath} --password {passwd}""",
        ).isProblematic():  return(icm.EH_badOutcome(outcome))

        print(vaultFilePath)

        return outcome

####+BEGIN: bx:icm:py3:method :methodName "vaultOpen" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultOpen/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultOpen(
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


####+BEGIN: bx:icm:py3:method :methodName "vaultGroupAdd" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultGroupAdd/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultGroupAdd(
####+END:
            self,
            vault,
            passwd,
            groupName,
    ):
        """ #+begin_org
*** TODO [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Add =groupName= to specified vault. Becomes persistent only when =passwd= is provided.
        #+end_org """

        kp = self.vaultOpen(vault, passwd)

        group = kp.add_group(kp.root_group, groupName)

        if passwd:
            kp.save()
        else:
            icm.ANN_write(f"Group -- {groupName} updated but not saved")

        return group


####+BEGIN: bx:icm:py3:method :methodName "vaultEntryUpdate" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultEntryUpdate/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultEntryUpdate(
####+END:
            self,
            vault,
            passwd,
            group,
            entryName,
            entryValue,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Create a new entry or update an exisiting one. Becomes persistent only when =passwd= is provided.
        #+end_org """

        kp = self.vaultOpen(vault, passwd)

        group = kp.find_groups(name=group, first=True)

        print(f"KKK {entryName}, {entryValue}")

        kp.add_entry(group, entryName, entryName, entryValue)
        #kp.add_entry(group, 'gmail', 'myusername', 'myPassw0rdXX')

        if passwd:
            kp.save()

        return kp

####+BEGIN: bx:icm:py3:method :methodName "vaultEntryRead" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultEntryRead/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultEntryRead(
####+END:
            self,
            vault,
            passwd,
            title,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  Return an entry given =title=.
        #+end_org """

        kp = self.vaultOpen(vault, passwd)

        entry = kp.find_entries(title=title, first=True)

        print(f"{title} -- {entry} {entry.username} {entry.password}")

        return entry

####+BEGIN: bx:icm:py3:method :methodName "vaultEntriesList" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultEntriesList/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultEntriesList(
####+END:
            self,
            vault,
            passwd,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| *MethodDesc:* | ]]  List existing entries.
        #+end_org """

        kp = self.vaultOpen(vault, passwd)

        print(f"Entries == {kp.entries}")

        return kp.entries




####+BEGIN: bx:icm:py3:method :methodName "vaultEntryDelete" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /vaultEntryDelete/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def vaultEntryDelete(
####+END:
            self,
            vault,
            passwd,
            title,
    ):
        """ #+begin_org
*** TODO [[elisp:(org-cycle)][| *MethodDesc:* | ]]  UnImpelemted. Delete the entry specified by =title=
        #+end_org """

        kp = pykeepass_cache.PyKeePass(self.vaultFilePath_obtain(vault), passwd,)
        return title, kp

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
        parDescription="Vault Name -- uniq within bpo/vault",
        parDataType=None,
        parDefault='fpVault',
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


####+BEGIN: bx:dblock:python:func :funcName "examples_bpo_vault" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList "oneBpo sectionTitle=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-examples [[elisp:(outline-show-subtree+toggle)][||]] /examples_bpo_vault/ =Show/Verify/Update For relevant PBDs= retType=none argsList=(oneBpo sectionTitle=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_bpo_vault(
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
        icm.cmndExampleMenuChapter('*Manage BPO Vault*')

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

    cmndName = "bpoVaultPrep"
    cmndArgs = ""
    cps = cpsInit() ; cps['bpoId'] = oneBpo ; cps['vault'] = vault ; cps['passwd'] = passwd
    menuItem(verbosity='none')

    cmndName = "bpoVaultList"
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

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultCreate" :parsMand "bpoId vault passwd" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultCreate>> parsMand=bpoId vault passwd parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultCreate(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', 'passwd', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Wrpper around class method.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        cmndOutcome = thisBpo.vaultCreate_wOp(vault, passwd, outcome=None)

        return cmndOutcome

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultOpen" :parsMand "bpoId vault passwd" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultOpen>> parsMand=bpoId vault passwd parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultOpen(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', 'passwd', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Wrpper around class method.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        thisBpo.vaultOpen(vault, passwd)

        return cmndOutcome


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultClose" :parsMand "" :parsOpt "vault" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultClose>> parsMand= parsOpt=vault argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultClose(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'vault', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        vault=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'vault': vault, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        vault = callParamsDict['vault']

####+END:
        self.cmndDocStr(f""" #+begin_org
** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]] UnImplemented -- Manually kill the server.
        #+end_org """)

        #pykeepass_cache.close()

        return cmndOutcome


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultGroupAdd" :parsMand "bpoId vault" :parsOpt "passwd" :argsMin "0" :argsMax "999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultGroupAdd>> parsMand=bpoId vault parsOpt=passwd argsMin=0 argsMax=999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultGroupAdd(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', ]
    cmndParamsOptional = [ 'passwd', ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Manually kill the server.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        # Any number of Name=Value can be passed as args
        for each in typing.cast(list, cmndArgs):
            group = thisBpo.vaultGroupAdd(vault, passwd, each)
            print(group)

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return typing.cast(dict, cmndArgsSpecDict)





####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultEntryUpdate" :parsMand "bpoId vault passwd" :parsOpt "" :argsMin "0" :argsMax "999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultEntryUpdate>> parsMand=bpoId vault passwd parsOpt= argsMin=0 argsMax=999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultEntryUpdate(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', 'passwd', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Manually kill the server.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        # Any number of Name=Value can be passed as args
        for each in typing.cast(list, cmndArgs):
            varNameValue = each.split('=')
            parValue=varNameValue[1]
            print(f"{varNameValue} {parValue}")
            thisBpo.vaultEntryUpdate(vault, passwd, 'bisos', varNameValue[0], varNameValue[1])

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return cmndArgsSpecDict




####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultEntryRead" :parsMand "bpoId vault" :parsOpt "passwd" :argsMin "0" :argsMax "999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultEntryRead>> parsMand=bpoId vault parsOpt=passwd argsMin=0 argsMax=999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultEntryRead(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', ]
    cmndParamsOptional = [ 'passwd', ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Manually kill the server.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        # Any number of Name=Value can be passed as args
        for each in typing.cast(list, cmndArgs):
            thisBpo.vaultEntryRead(vault, passwd, each)

        return cmndOutcome


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultEntriesList" :parsMand "bpoId vault" :parsOpt "passwd" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultEntriesList>> parsMand=bpoId vault parsOpt=passwd argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultEntriesList(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', ]
    cmndParamsOptional = [ 'passwd', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Manually kill the server.
        #+end_org """)

        thisBpo = BpoVault(bpoId,)

        thisBpo.vaultEntriesList(vault, passwd)

        return cmndOutcome





####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "vaultEntryDelete" :parsMand "" :parsOpt "vault" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<vaultEntryDelete>> parsMand= parsOpt=vault argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class vaultEntryDelete(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'vault', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        vault=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'vault': vault, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        vault = callParamsDict['vault']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Manually kill the server.
        #+end_org """)

        #pykeepass_cache.close()

        return cmndOutcome




####+BEGIN: bx:icm:py3:section :title "Secondary Command Services"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Secondary Command Services*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bpoVaultList" :parsMand "bpoId vault passwd" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<bpoVaultList>> parsMand=bpoId vault passwd parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class bpoVaultList(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'vault', 'passwd', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        vault=None,         # or Cmnd-Input
        passwd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'vault': vault, 'passwd': passwd, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        vault = callParamsDict['vault']
        passwd = callParamsDict['passwd']

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Wrpper around class method.
        #+end_org """)

        #thisBpo = BpoVault(bpoId,)

        #vaultBase = thisBpo.repoBasePrep()

        #thisBpo.vaulList(vault, passwd)

        return cmndOutcome



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "databasesList" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<databasesList>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class databasesList(icm.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Get a dictionary of currently cached databases.
        #+end_org """)

        # Should open the data bases first.
        dataBases = pykeepass_cache.cached_databases()

        print(dataBases)

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
