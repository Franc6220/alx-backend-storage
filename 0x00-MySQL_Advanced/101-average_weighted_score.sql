-- 101-average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update average_score for all users
    UPDATE users
    SET average_score = (
        SELECT 
            SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = users.id
    );
END //

DELIMITER ;

