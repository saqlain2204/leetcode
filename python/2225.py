'''
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
'''
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        dict = {}
        ans = []
        for match in matches:
            loser = match[1]
            if loser not in dict:
                dict[loser] = 1
            else:
                dict[loser] += 1

        winner_list = set()
        one_lost = set()
        for match in matches:
            winner = match[0]
            if winner not in dict.keys():
                winner_list.add(winner)
            if dict[match[1]] == 1:
                one_lost.add(match[1])

        winner_list = list(winner_list)
        one_lost = list(one_lost)
        winner_list.sort()
        one_lost.sort()
        ans.append(winner_list)
        ans.append(one_lost)

        return ans
    
'''
Constraints:
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.

Test case:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]

'''
print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(Solution().findWinners([[2,3],[1,3],[5,4],[6,4]]))