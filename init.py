import files.verifyFolders as dskTv
import config.cof as conf
import safety.safety as safety

dskTv = dskTv.VerifyFolders(conf.config["foldersForVerirify"])
dskTv()
safety = safety.safety(True, 4)
safety()