from .addUser import addUser
from .getUserIdByUsername import getUserIdByUsername
from .createAccount import createAccount
from .createHistoricalTransaction import createHistoricalTransaction

# needs Entitlements: CanCreateAccount
def bulkCreateUsers(numberOfUsers, numberOfTransactions, bankId, seedAccountId, seedBankId):

    for i in range(1, numberOfUsers + 1):
        username = "user" + i
        password = "aVery4long" + i
        addUser((username + "@openbankproject.com"), username, password, "Uli", "Name-" + username)
        userId = getUserIdByUsername(username)
        for y in range(1, 6):
            accountId = (str(username) + str(y) + "4bf2-11ea-87e6-54e1adfac5b1")
            createAccount(bankId, userId, "EUR", "autogenerated", "","", accountId)
            for x in range(1, numberOfTransactions + 1):
                createHistoricalTransaction(seedAccountId, seedBankId, accountId, bankId,
                                            "EUR", str(123 + x),"bulkcreated", '2019-09-19T02:11:29Z', "2019-09-20T02:31:28Z")










