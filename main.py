from smm import SMM

client = SMM(
    apikey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

print(
    "%s total services," % len(client.get_services()),
    "%s current balance" % client.get_balance()["balance"]
)