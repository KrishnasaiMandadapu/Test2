from config.imports import *
openai.api_key="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"
script_dir = os.path.dirname(os.path.abspath(__file__))

print(script_dir,end="???????????????")
# quest_data="/home/support/Semantic_search_3/Embeddings/quest.csv"

os.environ['_BARD_API_KEY'] = 'YAhoQ-pD09RoMqNeQxvntBfen4ybLmVDwZIP51bIt75C4EncYlEssopSSN0g0C8q3v8_7Q.'

token='YAhoQ-pD09RoMqNeQxvntBfen4ybLmVDwZIP51bIt75C4EncYlEssopSSN0g0C8q3v8_7Q.'
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

# root='/var/lib/jenkins/workspace/Python build/Test2/'
image= os.path.join(script_dir, 'resources', 'prodapt_image.png')
conversation_1= os.path.join(script_dir, 'history_logs', 'conversation_history.json')
conversation_2=os.path.join(script_dir, 'history_logs', 'conversation_history_bard.json')
# image=root+'resources/prodapt_logo.PNG'
# conversation_1=root+'history_logs/conversation_history.json'
# conversation_2=root+'history_logs/conversation_history_bard.json'
