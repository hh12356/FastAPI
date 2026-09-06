from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clazz` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `sno` INT NOT NULL COMMENT '学号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码',
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clazz_b1f07f24` FOREIGN KEY (`clas_id`) REFERENCES `clazz` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `tno` INT NOT NULL COMMENT '账号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '课程名',
    `teacher_id` INT NOT NULL COMMENT '课程讲师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4 COMMENT='学生选课表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmVtv2jAUx79K5KdNYlOgTaG8UdZq11Zq0TRpTJGTOCFqsJkv61jHd5/sODgJl5HSS0"
    "p56eX42LF/Pjnnb+cWjEmAEva2n8A/f0DXugUYjhHoWsWGhgXgZGLM0sChlyhPf+7iMU6h"
    "z0HXCmHCUMMCAWI+jSc8Jhh0LSySRBqJzziNcWRMAsc/BXI5iRAfIQq61vcfDQvEOEC/Ec"
    "v+nVy7YYySoDDROJDPVnaXTyfK9gHzM+Uon+a5PknEGBvnyZSPCJ57x5hLa4QwopAjOTyn"
    "Qk5fzk4vM1tROlPjkk4x1ydAIRQJzy3Xc40NuO75xcC9Oh24LqgAyCdYwo0xlzRuQSSn8K"
    "bVPGwfdg6ODjsNC6hpzi3tWfpoAybtqPCcD8BMtUMOUw/F2EBVvxew9keQLuea+ZfIMk7L"
    "ZDOO69BmBsPWxNPd4YKhaB+gYCjaCLaHwjm05d/HoQ02Qz6Gv90E4YiPJGfHWQP4a++y/7"
    "53+arlOK/l6IRCP31ZznVTK22bzWRchzqu54HuQf/6BtLALbSY7WFcBEjOa2GLTnTPs0+X"
    "KIFq5Yvbot/tq3SU+uzQxuGv0Rurfv0UTdIiq3AuNo1b47IFYhipJclnyydlqZAIytDSJJ"
    "m2rM+SxmefJvdpstZpsuOFaCja0PbSNPmkCbKRC2KOoD9C1K0UzMVO/w/q2qDveF5rKBxk"
    "d8CjRftCOVqAv0j+jFAUR/gTmqoN+IAZh9hfFug6Xw7MSDsBflU5aliAwpt5Mi5FIsFugB"
    "LE05zRu+r33p2C2eryv2Vt20Q9fIF4OiDy54Y7uYWEeIjCAIbC8Y6OhqLtNMOhOLbt42xn"
    "O52j7XdTrdotVf8cAyo1FwrmHmnRT0ETqrbpGk1ze6BDYb6JujXtpxv5iBIRjfK9jJhYGk"
    "QNC7jlMj1bq22yNSwRN7nlrVY3emJ7ebNT8oZhUoGq9q55gU3zg3MQth+vqOYlzOQmqKIY"
    "tXvNBaPj+TLpduxmbaTijkpz5zg4qJko9xPIqinyXI86Z4tHzcNrhLfEdQ+qe36V+8zobq"
    "quc1H1ZNI6L/i2U9bmTunFCmuDoKyrCyeYorAuSOeyri6q7u2FtWK/XllnZ90lyjp3DF6t"
    "rHOn7r2yflYZ/QVeHNZQnfBKZxjtXWdVIu+qgtb+DLOjZ5g7fQ9cKTuqfA68u+J4VpeyD/"
    "qNsIdo7I+WFXvdsrbWQ+OzL/W7Uup/Icr0e7dpwsx1qXPS3Bzxw5d5+VJVIKzdd5Bu07Y3"
    "oNu07ZV0VVvpiodgrq/3i4Q/Xl2cr7jjMV1KlIPY59ZfK4kZf763EeESuBKGHHnM2M8kz/"
    "TVl963Mu7+54sTBYcwHlE1ihrgpJoGuP9iNvsHIFPNJw=="
)
