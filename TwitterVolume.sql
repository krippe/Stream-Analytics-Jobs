SELECT 
    System.Timestamp AS Window, 
    COUNT (*) AS tot,
    SUM (CASE WHEN retweet = 1 then 1 else 0 end) as retw,
    SUM (CASE WHEN retweet = 0 then 1 else 0 end) as orig
INTO
    [PowerBiHour]
FROM
    [TwitterSWE] 
    TIMESTAMP BY DATEADD(millisecond, timestamp, '1970-01-01T00:00:00Z')
GROUP BY
    TumblingWindow(hour, 1), Count
