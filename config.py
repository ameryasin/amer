import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "ameeuu"))
API_HASH = os.getenv("API_HASH", "321d6229991a110ab7d6a28910be3286")
SESSION = os.getenv("1BJWap1wBu2S7tv_MOpGhD3ONAS1TvzmuR_k3CtZyRnTupri8dIb5I3ZDpF6nlM_B79-Yqs_wlKPSP_H1aCE2NBsgGhaww0EXMJd3rFJkSLrNWMpboOcEJkRDnwMITou4WGvkZ8VCUC6_gH951iYA2qAtumHtU9Nc6F1FXiLz5bFtH2fCHypeVdBD4FV9hK11pPKfqkDqF9Sn6pvC2KgOlJYbRzbZE2sJpTktPH-RxzPOqBwvu_pKIY6OhmzWAu_CdL_FmM6oMDuFP-SQuLNWyas-8O0fp5IeRwjuoVELovnaYT25pZ-n-DEfyPMKn-Pbk2FgmA3HcsFAOZnKJVguDeBpf135BSc=")
HNDLR = os.getenv("HNDLR", "!")

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
