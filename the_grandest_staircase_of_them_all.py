#!/usr/bin/env python

# todo, can be more percise
def answer(n):
    dp = [[0 for _ in xrange(n)] for _ in xrange(n + 1)]
    dp[3][2] = 1

    for j in [0, 1, 2]:
        for i in xrange(j, n):
            dp[j][i] = 1

    for i in xrange(3, n + 1):
        for bot in xrange(2, n):
            if i == 3 and bot == 2:
                continue
            if bot > i:
                dp[i][bot] = dp[i][bot - 1]
            else:
                dp[i][bot] = dp[i][bot-1] + dp[i - bot][bot - 1]

            # print '(%d, %d)[%d] = (%d, %d)[%d] + (%d, %d)[%d]' % (i, bot,dp[i][bot], i, bot - 1,dp[i][bot-1], i -
            #                                                       bot, bot - 1,
            #                                                       dp[i-bot][bot -
            #                                                               1])

    # for i in dp:
    #     print i
    # print

    return dp[n][n-1]


#for i in xrange(3, 10):
print answer(200)
