import files.verifyFolders as dskTv
import config.cof as conf
import asyncio
import safety.safety as safety
import saudacao.hello as saudacao

async def fundskTv():
    if saudacao.saudacao():
        dsk = dskTv.VerifyFolders(conf.config["foldersForVerirify"], True)
        await dsk()

async def funsafety():
    saf = safety.safety(True, 4)
    await saf()

async def main():
    f1 = asyncio.create_task(fundskTv())
    f2 = asyncio.create_task(funsafety())
    await asyncio.wait([f1, f2])

asyncio.run(main())