# Group Project Resources:

1. 实用的例子：
https://zhuanlan.zhihu.com/p/32677267
d3js财务数据可视化实战攻略(0)
- 例子的网站http://qiou.eu/v/#/
- 例子2http://qiou.eu/v2/#/

Teach you to draw a Pie Chart: (Tecent Tutorial)
    https://cloud.tencent.com/developer/article/1020344

D3 Chinese API document:
https://github.com/d3/d3/wiki/API--%E4%B8%AD%E6%96%87%E6%89%8B%E5%86%8C

D3 Examples:
https://bl.ocks.org/mbostock



Another Game Analysis resources:
    https://www.kaggle.com/lhy1989/learn-from-steam-users-and-games-eda
    https://www.kaggle.com/phaethonprime/non-negative-recommended-system/notebook

Steam Game Searching API:
https://steamspy.com/about
https://steamspy.com/api.php
    API Requests:
    - Return the Game List which tag is "Racing"
        - http://steamspy.com/api.php?request=tag&tag=Racing
    - Return top 100 games in 2 weeks
        - http://steamspy.com/api.php?request=top100in2weeks

    ## Data Information:
    * appid - Steam Application ID. If it's 999999, then data for this application is hidden on developer's request, sorry.
    * name - the game's name
    * developer - comma separated list of the developers of the game
    * publisher - comma separated list of the publishers of the game
    * score_rank - score rank of the game based on user reviews
    * positive - number of positive user reviews
    * negative - number of negative user reviews
    * userscore - user score of the game
    * owners - owners of this application on Steam. **Beware of free weekends!**
    * owners_variance - variance in owners. The real number of owners lies somewhere on owners +/- owners_variance range.   
    * players_forever - people that have played this game since March 2009.
    * players_forever_variance - variance for total players.
    * players_2weeks - people that have played this game in the last 2 weeks.
    * players_2weeks_variance - variance for the number of players in the last two weeks.
    * average_forever - average playtime since March 2009. In minutes.
    * average_2weeks - average playtime in the last two weeks. In minutes.
    * median_forever - median playtime since March 2009. In minutes.
    * median_2weeks - median playtime in the last two weeks. In minutes.
    * price - US price in cents.

    * ccu - peak CCU yesterday (only returned if an individual app is requested).
    * tags - the game's tags with votes in JSON array (only returned if an individual app is requested).

-------

# Log:
2018/4/6:
Showing that in console:
Object { 10: Object, 240: Object, 440: Object, 550: Object, 570: Object, 620: Object, 730: Object, 4000: Object, 8930: Object, 22380: Object, 90 more… }
