class Solution:
    def myDFS(pathForNodes, remainTickets, startPosition, resultList):
        resultList.append(startPosition)
        if len(remainTickets) == 0:
            return True
        availableList = []
        if(pathForNodes.__contains__(startPosition)):
            availableList = pathForNodes[startPosition]
        for node in availableList:
            if [startPosition,node] not in remainTickets:
                continue

            remainTickets.remove([startPosition,node])
            if Solution.myDFS(pathForNodes, remainTickets, node,resultList):
                return True
            remainTickets.append([startPosition,node])

        resultList.pop(-1)
        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pathForNodes = dict()
        remainTickets = []
        resultList = []
        for ticket in tickets:
            if pathForNodes.__contains__(ticket[0]):
                pathForNodes[ticket[0]].append((ticket[1]))
            else:
                pathForNodes[ticket[0]] = [ticket[1]]
            
            remainTickets.append(ticket)
        
        for i in pathForNodes.keys():
            pathForNodes[i].sort()

        Solution.myDFS(pathForNodes,remainTickets,"JFK",resultList)
        return resultList