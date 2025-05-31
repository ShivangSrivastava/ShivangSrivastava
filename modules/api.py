import requests


class ApiManager:
    def __init__(self):
        self.__USERNAME = "ShivangSrivastava"
        self.__BASE_URL = "https://api.github.com"
        self.__STAR_URL = "https://api.github-star-counter.workers.dev"
        self.__user_response = None
        self.__star_response = None
        self.__repo_response = None
        self.__commits = None
        self.__language_count = {}

    @property
    def most_used_language(self):
        sorted_languages = sorted(
            self.__language_count.items(), key=lambda item: item[1], reverse=True
        )

        lang_lst = [language for language, count in sorted_languages]
        s = ""
        i = 0
        while len(s) + len(lang_lst[i]) < 35 and i < len(lang_lst):
            if not i:
                s = lang_lst[i]
            else:
                s = f"{s}, {lang_lst[i]}"
            i += 1
        return s

    @property
    def followers_count(self):
        return self.__user_response.get("followers", 0)

    @property
    def following_count(self):
        return self.__user_response.get("following", 0)

    @property
    def bio(self):
        full_bio = self.__user_response.get("bio", "New user")
        if len(full_bio) > 45:
            return f"{full_bio[:45]}..."
        return full_bio

    @property
    def public_repos(self):
        return self.__user_response.get("public_repos", 0)

    @property
    def stars(self):
        return self.__star_response.get("stars", 0)

    @property
    def commits(self):
        return self.__commits

    def setup(self):
        self.__update_response()
        self.__count_commits()
        self.__get_language()

    def __count_commits(self):
        total_commits = 0
        repos_data = self.__repo_response

        for repo in repos_data:
            commits_url = repo["commits_url"].replace("{/sha}", "")
            commits_response = requests.get(commits_url)
            total_commits += len(commits_response.json())
        self.__commits = total_commits

    def __get_language(self):
        excluded = {"HTML", None, "Jupyter Notebook", "Brainfuck"}
        repos_data = self.__repo_response
        for repo in repos_data:
            language = repo.get("language")
            if language in excluded:
                continue
            if language in self.__language_count:
                self.__language_count[language] += 1
            else:
                self.__language_count[language] = 1

    def __update_response(self):
        url = f"{self.__BASE_URL}/users/{self.__USERNAME}"
        self.__user_response = requests.get(url).json()

        star_url = f"{self.__STAR_URL}/user/{self.__USERNAME}"
        self.__star_response = requests.get(star_url).json()

        repo_url = f"{self.__BASE_URL}/users/{self.__USERNAME}/repos"
        self.__repo_response = requests.get(repo_url).json()
