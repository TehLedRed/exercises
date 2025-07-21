from exercises.gradeSchool import School


def test_roster() -> None:
    anglo = School()
    anglo.enroll("Charlie", 2)
    anglo.enroll("Bob", 1)
    anglo.enroll("Ana", 1)
    assert anglo.roster() == ["Ana", "Bob", "Charlie"]


def test_no_repeated_name() -> None:
    anglo = School()
    anglo.enroll("Charlie", 2)
    anglo.enroll("Charlie", 1)
    assert anglo.roster() == ["Charlie"]


def test_roster_is_empty_when_no_student_is_added() -> None:
    school = School()

    assert [] == school.roster()


def test_add_a_student() -> None:
    school = School()

    school.enroll(name="Aimee", grade=2)

    assert [True] == school.added()


def test_student_is_added_to_the_roster() -> None:
    school = School()

    school.enroll(name="Aimee", grade=2)

    assert ["Aimee"] == school.roster()


def test_adding_multiple_students_in_the_same_grade_in_the_roster() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="Paul", grade=2)

    assert [True, True, True] == school.added()


def test_multiple_students_in_the_same_grade_are_added_to_the_roster() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.roster()


def test_cannot_enroll_to_same_grade_in_the_roster_more_than_once() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="Paul", grade=2)

    assert [True, True, False, True] == school.added()


def test_student_not_added_to_same_grade_in_the_roster_more_than_once() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.roster()


def test_adding_students_in_multiple_grades() -> None:
    school = School()

    school.enroll(name="Chelsea", grade=3)
    school.enroll(name="Logan", grade=7)

    assert [True, True] == school.added()


def test_students_in_multiple_grades_are_added_to_the_roster() -> None:
    school = School()

    school.enroll(name="Chelsea", grade=3)
    school.enroll(name="Logan", grade=7)

    assert ["Chelsea", "Logan"] == school.roster()


def test_cannot_add_same_student_to_multiple_grades_in_the_roster() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=3)
    school.enroll(name="Paul", grade=3)

    assert [True, True, False, True] == school.added()


def test_student_not_added_to_multiple_grades_in_the_roster() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=3)
    school.enroll(name="Paul", grade=3)

    assert ["Blair", "James", "Paul"] == school.roster()


def test_students_are_sorted_by_grades_in_the_roster() -> None:
    school = School()

    school.enroll(name="Jim", grade=3)
    school.enroll(name="Peter", grade=2)
    school.enroll(name="Anna", grade=1)

    assert ["Anna", "Peter", "Jim"] == school.roster()


def test_students_are_sorted_by_name_in_the_roster() -> None:
    school = School()

    school.enroll(name="Peter", grade=2)
    school.enroll(name="Zoe", grade=2)
    school.enroll(name="Alex", grade=2)

    assert ["Alex", "Peter", "Zoe"] == school.roster()


def test_students_are_sorted_by_grades_and_then_by_name_in_the_roster() -> None:
    school = School()

    school.enroll(name="Peter", grade=2)
    school.enroll(name="Anna", grade=1)
    school.enroll(name="Barb", grade=1)
    school.enroll(name="Zoe", grade=2)
    school.enroll(name="Alex", grade=2)
    school.enroll(name="Jim", grade=3)
    school.enroll(name="Charlie", grade=1)

    assert ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"] == school.roster()


def test_grade_is_empty_if_no_students_in_the_roster() -> None:
    school = School()

    assert [] == school.consult(1)


def test_grade_is_empty_if_no_students_in_that_grade() -> None:
    school = School()

    school.enroll(name="Peter", grade=2)
    school.enroll(name="Zoe", grade=2)
    school.enroll(name="Alex", grade=2)
    school.enroll(name="Jim", grade=3)

    assert [] == school.consult(1)


def test_student_not_added_to_same_grade_more_than_once() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.consult(2)


def test_student_not_added_to_multiple_grades() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=3)
    school.enroll(name="Paul", grade=3)

    assert ["Blair", "James"] == school.consult(2)


def test_student_not_added_to_other_grade_for_multiple_grades() -> None:
    school = School()

    school.enroll(name="Blair", grade=2)
    school.enroll(name="James", grade=2)
    school.enroll(name="James", grade=3)
    school.enroll(name="Paul", grade=3)

    assert ["Paul"] == school.consult(3)


def test_students_are_sorted_by_name_in_a_grade() -> None:
    school = School()

    school.enroll(name="Franklin", grade=5)
    school.enroll(name="Bradley", grade=5)
    school.enroll(name="Jeff", grade=1)

    assert ["Bradley", "Franklin"] == school.consult(5)
