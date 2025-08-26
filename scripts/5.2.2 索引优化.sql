-- 用户表索引
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_role ON users(role);

-- 题目表索引
CREATE INDEX idx_questions_subject_id ON questions(subject_id);
CREATE INDEX idx_questions_difficulty ON questions(difficulty);
CREATE INDEX idx_questions_created_at ON questions(created_at);

-- 作业分配表索引
CREATE INDEX idx_homework_assignments_homework_id ON homework_assignments(homework_id);
CREATE INDEX idx_homework_assignments_student_id ON homework_assignments(student_id);
CREATE INDEX idx_homework_assignments_status ON homework_assignments(status);