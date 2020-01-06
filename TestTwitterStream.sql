SELECT
    timestamp, DATEADD(millisecond, timestamp, '1970-01-01T00:00:00Z') AS time, lang, tweet_id, user_id, tweet, user_name, retweet, retweeted_id, retweeted_user_id, in_reply_to AS inreplyto, hashtags
INTO
    [TweetsToBlob]
FROM
    [TwitterStreamIn]
