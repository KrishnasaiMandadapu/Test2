from config.imports import *

openai.api_key="krishna"

current_directory = os.getcwd()

#print(script_dir,end="???????????????")
# quest_data="/home/support/Semantic_search_3/Embeddings/quest.csv"

os.environ['_BARD_API_KEY'] = 'krishna'

token=''
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

root=current_directory

# image= os.path.join(script_dir, 'resources', 'prodapt_image.png')
# conversation_1= os.path.join(script_dir, 'history_logs', 'conversation_history.json')
# conversation_2=os.path.join(script_dir, 'history_logs', 'conversation_history_bard.json')
image=root+'/resources/prodapt_logo.PNG'
conversation_1=root+'/history_logs/conversation_history.json'
conversation_2=root+'/history_logs/conversation_history_bard.json'
