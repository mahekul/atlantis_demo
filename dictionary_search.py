import requests


class DictionaryClass():
    def __init__(self):
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/{}"

    def search(self, word):
        meaning = []
        response = requests.get(self.url.format(word))
        if response.status_code == 200:
            data = response.json()
            meaning.append(data[0].get("word"))
            for i in data[0].get("meanings"):
                if i.get("partOfSpeech") == "noun":
                    meaning.append(i.get("partOfSpeech"))
                    meaning.append(i.get("definitions")[0].get("definition"))
        return " ".join(meaning)


if "__main__" == __name__:
    word = input("Word?")
    dict_obj = DictionaryClass()
    print(dict_obj.search(word))
