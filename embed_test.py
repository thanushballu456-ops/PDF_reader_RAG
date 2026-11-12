from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

chunks = [
    """MUDUNURI SREEJA
Software Engineer
[/ne+91-8179662888sreejaraazu2005@gmail.comHydrabad](mailto:/ne+91-8179662888sreejaraazu2005@gmail.comHydrabad) - India/♀nednLinkedin/gtbGithub Leetcode
EDUCATION
B.T ech. (CSE) - 8.8 CGPA
Uttranchal Institute of T echnology
Ὄ2023 – presentDehradun, Uttarakhand
Higher Secondary - 94%
Narayana Junior College
Ὄ2023Hydrabad, T elangana
Secondary - 9.7 CGPA
Vedant High School
Ὄ2021Hydrabad, T elangana
PROJECTS
AI-Resume-Portfolio-Builder
•ReactJs | Python | Fetch API | Uvicorn | Ope-
nAI gpt - 3.5/ GPT model -4
•Developed an AI-powered Resume Builder
using NLP and machine learning models to
auto-generate resume content, optimize skills,
and ensure ATS compliance.
•Implemented a full-stack system using Python,
FastAPI, React, and MongoDB, integrating
AI text generation for personalized and job-
speciﬁc resume suggestions""",

    """ted a full-stack system using Python,
FastAPI, React, and MongoDB, integrating
AI text generation for personalized and job-
speciﬁc resume suggestions. Github
Email Summerization
•n8n | API Key | Automation nodes
•Built an automated email summarization work-
ﬂow using n8n, integrating NLP models to
extract key points and generate concise sum-
maries from incoming emails.
•Implemented real-time email processing with
n8n, enhancing productivity by automatically
categorizing, summarizing, and forwarding
important insights to users. Github
Weather Updates
•n8n | Whatsapp API Key | Automation nodes
•Created an automated n8n workﬂow to fetch
real-time weather data from APIs and deliver
daily weather notiﬁcations to users.
•Integrated API triggers and schedulers in n8n
to send location-based weat""",

    """ime weather data from APIs and deliver
daily weather notiﬁcations to users.
•Integrated API triggers and schedulers in n8n
to send location-based weather alerts through
WhatsApp .
•Implemented data parsing and format-
ting nodes to generate clean, user-friendly
weather summaries for quick insights.
•Optimized workﬂow reliability by adding
error-handling and fallback steps, ensuring
uninterrupted delivery of weather updates.
Github
EXPERIENCE
SDE Intern
ITJOBXS
ὌOct 2025 – PresentRemote, India
•Designed and developed a fully responsive web page for the
Interview Experiences page accessibilty user experience and
page accessibility
•Worked on user veriﬁcation and authentication system to de-
tect and remove fake botigistration, strengthening plat form
security and ensuring data integrity.
IBM"""
]

embeddings = model.encode(chunks)

print("Embedding shape:", embeddings.shape)
print("Number of chunks:", len(chunks))
print("First vector length:", len(embeddings[0]))
print("First 10 values:", embeddings[0][:10])

