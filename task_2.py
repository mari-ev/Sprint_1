class Tester:
    def __init__(self, name: str):
        self.name = name

    def work_hard(self, deadline: bool = True):
        test_vibe = 'Что ж, ещё часок поработаю!' if deadline else 'Можно отдыхать'
        print(f"{self.name} {test_vibe}")

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!' 