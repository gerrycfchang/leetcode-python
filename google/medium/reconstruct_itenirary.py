
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(dest, conn, res, tickets):
            if len(res) == len(tickets) + 1: return res
            currentDst = sorted(conn[dest])
            for airport in currentDst:
                res.append(airport)
                conn[dest].remove(airport)
                valid = dfs(airport, conn, res, tickets)
                if valid: return res
                res.pop()
                conn[dest].append(airport)

        res, conn = [], defaultdict(list)
        for ticket in tickets:
            if ticket[0] not in conn:
                conn[ticket[0]] = [ticket[1]]
            else:
                conn[ticket[0]].append(ticket[1])
        res.append('JFK')
        res = dfs('JFK', conn, res, tickets)
        return res
                

if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert sol.findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    tickets = [["JFK","ATL"],["ATL","JFK"]]
    assert sol.findItinerary(tickets) == ["JFK","ATL","JFK"]

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    assert sol.findItinerary(tickets) == ["JFK","NRT","JFK","KUL"]

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    exp     = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert sol.findItinerary(tickets) == exp

    tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
    exp = ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
    assert sol.findItinerary(tickets) == exp