from modules.api import ApiManager
from modules.svg import SVGTextModifier
from modules.utils import SVG_ID, get_current_datetime

FILE_NAME = "terminal.svg"


stm = SVGTextModifier(FILE_NAME)

apim = ApiManager()
apim.setup()

stm.modify_text(id_name=SVG_ID.last_login, new_value=get_current_datetime())

stm.modify_text(id_name=SVG_ID.follower_count, new_value=apim.followers_count)

stm.modify_text(id_name=SVG_ID.following_count, new_value=apim.following_count)
stm.modify_text(id_name=SVG_ID.bio, new_value=apim.bio)
stm.modify_text(id_name=SVG_ID.repo_count, new_value=apim.public_repos)
stm.modify_text(id_name=SVG_ID.star_count, new_value=apim.stars)
stm.modify_text(id_name=SVG_ID.commit_count, new_value=apim.commits)
stm.modify_text(id_name=SVG_ID.language, new_value=apim.most_used_language)

stm.save(FILE_NAME)
