from datetime import datetime


def get_current_datetime():
    return datetime.now().strftime("%a %b %d %H:%M:%S %Y on tty1")


class SVG_ID:
    last_login = "last-login"
    follower_count = "followers-count"
    following_count = "following-count"
    bio = "bio"
    repo_count = "repo-count"
    star_count = "stars-count"
    commit_count = "commits-count"
    language = "language"
