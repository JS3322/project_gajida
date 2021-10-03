import luigi


class CountLetters(luigi.Task):
    def requires(self):
        return luigi_GenerateWords()  # txt 파일생성

    def output(self):  # temp_letter_counts.txt에 저장
        return luigi.LocalTarget("temp_letter_counts.txt")

    def run(self):  # 테스크 실행
        # 줄마다 잘라서 배열에 저장
        with self.input().open("r") as infile:
            words = infile.read().splitlines()

        # 줄마다 이름 길이 계산
        with self.output().open("w") as outfile:
            for word in words:
                outfile.write(
                    "{word} | {letter_count}\n".format(
                        word=word, letter_count=self.counter(word)
                    )
                )  # 예) "Sabrina Bates | 12" 형식으로 output

    @staticmethod
    def counter(word):  # 공백 제거 후 길이 return
        word = word.replace(" ", "")
        return len(word)
