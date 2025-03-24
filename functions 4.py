# TC03V7DGN3 Confirmed . ksh3,000 sent to FRANCIS KITUNGI on 24/3.25 at 8.02AM.

def extract_amount(mpesa_message):
    index_ksh = mpesa_message.index('ksh')
    index_sent = mpesa_message.index('Sent')
    amount = mpesa_message[index_ksh: index_sent]

    #ksh3,000
    amount = amount.replace('ksh ', '')
    amount = amount.replace(', ', '')
    print(amount)

    def extraxt_date(mpesa_message):
        index_on = mpesa_message.index('on')
        index_at = mpesa_message.index('at')
        date = mpesa_message[index_on: index_at]
print(date)


message_1 = "# TC03V7DGN3 Confirmed .ksh3,000 sent to FRANCIS Simeon on 24/3.25 at 8.02AM."
extract_amount(message_1)


