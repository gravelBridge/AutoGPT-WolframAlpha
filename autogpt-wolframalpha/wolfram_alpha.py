# The main code for the AutoGPT Wolfram Alpha plugin.

import os
import wolframalpha

API_URL = "https://api.wolframalpha.com/v2/query"
APP_ID = ""

def wolfram_alpha_app_id_set():
    global APP_ID

    if os.getenv("WOLFRAM_ALPHA_APP_ID"):
        APP_ID = os.getenv("WOLFRAM_ALPHA_APP_ID")
        return True
    
    return False

def make_query(prompt):
    client = wolframalpha.Client(APP_ID)

    res = client.query(prompt)

    answer = next(res.results).text

    return answer