from static.vuln_notify import vuln_found_notify


def potential_verbose_message(message, url="default"):
    verbose = False
    if verbose:
        if message == "ERROR":
            print(f"[VERBOSE] Request Error for {url}")
        elif message == "CANARY":
            print(f"[VERBOSE] CANARY reflection in {url}. Confirming cache poisoning in progress ...")
        elif message == "STATUS_CODE":
            print(f"[VERBOSE] STATUS_CODE difference in {url}. Confirming cache poisoning in progress ...")
        elif message == "LENGTH":
            print(f"[VERBOSE] LENGTH difference in {url}. Confirming cache poisoning in progress ...")
        elif message == "UNSUCCESSFUL":
            print(f"[VERBOSE] Unsuccessful vulnerability confirmation on {url}\n")
        elif message == "CRAWLING":
            print(f"[VERBOSE] Crawling. Scanning : {url}")

def behavior_or_confirmed_message(uri, behaviorOrConfirmed, behaviorType, explicitCache, url, status_codes="default", header = "default", outputFile = "default", LOCK = "default"):

    messageDict = {"REFLECTION": "HEADER REFLECTION",
                   "STATUS": "DIFFERENT STATUS-CODE: {}".format(status_codes),
                   "LENGTH": "DIFFERENT RESPONSE LENGTH",
                   "BEHAVIOR": "[INTERESTING BEHAVIOR]",
                   "CONFIRMED": "VULNERABILITY CONFIRMED"
                   }

    if header != "default":
        message = f" └── \033[31m{messageDict[behaviorOrConfirmed]}\033[0m | {messageDict[behaviorType]} | EXPLICIT CACHE : {explicitCache} | \033[34m{uri}\033[0m | PAYLOAD : {header}"
        print(message)
        if behaviorOrConfirmed != "BEHAVIOR":
            vuln_found_notify(uri, header)
    else:
        message = f" └── \033[31m{messageDict[behaviorOrConfirmed]}\033[0m | PORT {messageDict[behaviorType]} | EXPLICIT CACHE : {explicitCache} | \033[34m{uri}\033[0m | PAYLOAD : {header}"
        print(message)
        if behaviorOrConfirmed != "BEHAVIOR":
            vuln_found_notify(uri, header)
