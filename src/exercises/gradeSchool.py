from os import name


class School:
    def __init__(self) -> None:
        self.students: dict[int, list[str]] = {}
        self.enrollment: list[bool] = []

    def roster(self) -> list[str]:
        return [name
                for grade in sorted(self.students.keys())
                for name in sorted(self.students[grade])]

    def enroll(self, name: str, grade: int) -> None:
        if name not in set(self.roster()):
            self.students[grade] = self.students.get(grade, []) + [name]
            self.enrollment.append(True)
        else:
            self.enrollment.append(False)

    def consult(self, grade: int) -> list[str]:
        return sorted(self.students.get(grade, []))

    def added(self) -> list[bool]:
        return self.enrollment
