class Employee:
    def __init__(self, f_name, l_name, age, job_title):
        self._f_name = f_name
        self._l_name = l_name
        if age < 18:
            raise ValueError("Too young!")
        self._age = age
        self._job_title = job_title

    def __repr__(self):
        return f"{self._f_name}, {self._l_name}, {self._age}, {self._job_title}"

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self, value):
        self._f_name = value

    @property
    def l_name(self):
        return self._l_name

    @f_name.setter
    def f_name(self, value):
        self._l_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


    @property
    def job_title(self):
        return self._job_title