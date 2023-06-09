"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

e.g
ranked=[100, 90, 90, 80]
player_scores=[70, 80, 105]

The ranked players will have ranks 1, 2, 2, and 3, respectively.
If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st.
So return [4,3,1]
"""

# Problem Solution
def climbingLeaderboard(ranked, player_scores):
    # Write your code here
    scores=sorted(set(ranked),reverse=True)
    index=len(scores)-1
    answer=[]
    for i in player_scores:
        while(index>=0 and i>=scores[index]):
            index-=1
        answer.append(index+2)
    return answer

climbingLeaderboard([100, 90, 90, 80], [70, 80, 105])