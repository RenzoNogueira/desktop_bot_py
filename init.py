import files.verifyFolders as dskTv
import confing.cof as conf

deskTopVerify = dskTv.VerifyFolders(conf.confing["foldersForVerirify"])
print(deskTopVerify.listFiles(conf.confing["foldersForVerirify"]))