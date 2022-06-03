import files.verifyFolders as dskTv
import config.cof as conf
import safety.safety as safety
import saudacao.hello as saudacao

if saudacao.saudacao():
    dskTv = dskTv.VerifyFolders(conf.config["foldersForVerirify"])
    dskTv()

safety = safety.safety(True, 4)
safety()