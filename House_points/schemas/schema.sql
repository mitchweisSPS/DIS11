DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id        STRING PRIMARY KEY,
    student_firstname STRING,
    student_lastname  STRING,
    student_email     STRING,
    student_password  STRING,
    student_year      INT,
    student_points    INT
);
