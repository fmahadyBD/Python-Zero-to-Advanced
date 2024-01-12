# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #convert the map object to a list and sort descending order
    scores = sorted(list(arr), reverse=True)
    #Find the uniquq runner-up score
    runner_up_score=next(score for score in scores if score<max(scores))
    print(runner_up_score)
