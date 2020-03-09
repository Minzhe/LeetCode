SELECT Score, (
    SELECT COUNT(DISTINCT Score) FROM Scores 
    WHERE Score >= s.Score
) RANK
FROM Scores s
ORDER BY Score DESC