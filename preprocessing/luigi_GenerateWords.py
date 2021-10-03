from faker import Faker


class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget("temp_words.txt")
        # temp_words.txt에 저장
        # 자동으로 CountLetters의 input이 된다.

    def run(self):
        fake = Faker()
        names = [fake.name() for _ in range(1000)]  # faker를 통한 미국식 이름 랜덤 생성
        with self.output().open("w") as f:
            for name in names:
                f.write("{word}\n".format(word=name))
