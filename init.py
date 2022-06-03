import files.verifyFolders as dskTv
import confing.cof as conf
import saudacao.hello as saudacao

if saudacao.saudacao():
    deskTopVerify = dskTv.VerifyFolders(conf.confing["foldersForVerirify"])