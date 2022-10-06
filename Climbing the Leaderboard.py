def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    player.sort(reverse=True)
    ranked.sort(reverse=True)
    n = len(ranked)
    last = 0
    ans = []
    for i in range(n):
        for j in range(last, len(player)):
            if player[j]>ranked[i]:
                ans.append(i+1)
                last+=1
            elif player[j]==ranked[i]:
                ans.append(i+1)
                last+=1
            else: break
    if len(ans)<len(player):
        for i in range(last, len(player)):
            ans.append(len(ranked)+1)
            
    return ans[::-1]

ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)
print(result)