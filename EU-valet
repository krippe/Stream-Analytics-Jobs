WITH selection AS (
    SELECT *
    FROM [euvalet]
    TIMESTAMP BY DATEADD(millisecond, timestamp, '1970-01-01T00:00:00Z')
    WHERE
        tweet LIKE LOWER('%eu%') 
        )

SELECT
    System.Timestamp AS Window,
    COUNT (*) AS tot,
    SUM (CASE WHEN retweet = 1 then 1 else 0 end) as retw,
    SUM (CASE WHEN retweet = 0 then 1 else 0 end) as orig

INTO
    [eu-valet]

FROM
    selection AS event

GROUP BY
    TumblingWindow(hour, 1), Count
