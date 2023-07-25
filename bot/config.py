import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"

# 언어설정
with open(config_dir / "language.yml", 'r') as f:
    language_yaml = yaml.safe_load(f)
    
current_language = language_yaml["current_language"]
# chat_modes
if current_language == "kr":
    mod_config_file = "chat_modes_kr.yml"
else:
    mod_config_file = "chat_modes_en.yml"
    
with open(config_dir / mod_config_file, 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
# languages
help_msg = language_yaml[current_language]["HELP_MESSAGE"]
help_group_chat_msg = language_yaml[current_language]["HELP_GROUP_CHAT_MESSAGE"]
hi_msg = language_yaml[current_language]["HI_MESSAGE"]
timeout_msg = language_yaml[current_language]["TIMEOUT_MESSAGE"]
empty_retry_msg = language_yaml[current_language]["EMPTY_RETRY_MESSAGE"]
failed_edit_msg = language_yaml[current_language]["FAILED_EDIT_MESSAGE"]
input_err_msg = language_yaml[current_language]["INPUT_ERR_MESSAGE"]
err_toolong_msg = language_yaml[current_language]["ERR_TOOLONG_MESSAGE"]
first_delete_msg = language_yaml[current_language]["FIRST_DELETE_MESSAGE"]
n_first_delete_msg = language_yaml[current_language]["NFIRST_DELETE_MESSAGE"]
new_dialog_msg = language_yaml[current_language]["NEW_DIALOG_MESSAGE"]
cancel_msg = language_yaml[current_language]["CANCEL_MESSAGE"]
nothing_cancel_msg = language_yaml[current_language]["NOTHING_CANCEL_MESSAGE"]
start_dialog_msg = language_yaml[current_language]["START_DIALOG_MESSAGE"]
