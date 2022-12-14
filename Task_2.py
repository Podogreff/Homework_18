class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __name__(self):
        return self.name

    def __repr__(self):
        return f'Boss name is: {self.name}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            print(f'{new_boss.name} is not a boss, please enter another name')

    def __name__(self):
        return self.name

    def __repr__(self):
        return f'- worker id: {self.id};\n' \
               f'- worker name: {self.name};\n' \
               f'- worker company: {self.company};\n' \
               f'- worker boss: {self.boss}.'


boss_1 = Boss(1001, 'Vladyslav', 'Google')
boss_2 = Boss(1002, 'Andriy', 'Google')
worker_1 = Worker(9999, 'Dima', 'Google', boss_1)
worker_2 = Worker(9998, 'Oleg', 'Google', boss_2)
print(worker_2)
print(boss_2)
