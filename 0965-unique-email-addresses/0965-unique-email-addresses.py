class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #If '.' in local name (before the @), remove the '.'
        #If '+' in local name, everything after the FIRST '+' will be ignored

        someDict = {}
        for email in emails:
            indexFinder = email.find("@")
            localName = email[:indexFinder]
            if "." in localName:
                localName = localName.replace(".", "")

            if "+" in localName:
                plusFinder = localName.find("+")
                localName = localName[:plusFinder]

            domainName = email[indexFinder + 1:]

            if domainName not in someDict:
                someDict[domainName] = {localName}
            else:
                temp = someDict[domainName]
                temp.add(localName) 
                someDict[domainName] = temp

        result = 0
        for domain in someDict:
            result += len(someDict[domain])
            
        return result