import json
import os
import openai
import sys

# Set your API key securely — use env var or .env loader
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(job_title, company, job_url, job_description):
    return (
        f"Generate a LinkedIn post for {job_title} at {company}\n\n"
        f"Job Description:\n{job_description}\n\n"
        f"The job link is: {job_url}"
    )

def format_to_jsonl(job_title, company, job_url, job_description, post_text):
    return {
        "messages": [
            {
                "role": "system",
                "content": "You are a LinkedIn content generator that generates LinkedIn Posts for recruiter."
            },
            {
                "role": "user",
                "content": build_prompt(job_title, company, job_url, job_description)
            },
            {
                "role": "assistant",
                "content": post_text
            }
        ]
    }

def generate_with_gpt(prompt):
    print("🤖 Generating LinkedIn post with GPT-4...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a LinkedIn content generator that generates LinkedIn Posts for recruiter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return ""

def collect_job_post(auto_generate=False):
    print("\nNew Job Post Entry\n")
    job_title = input("Job Title: ")
    company = input("Company Name: ")
    job_url = input("Job URL: ")

    print("\nPaste the job description below. When you're done, press:")
    print(" - Ctrl+D (Mac/Linux) OR")
    print(" - Ctrl+Z then Enter (Windows)\n")
    job_description = sys.stdin.read().strip()

    if auto_generate:
        prompt = build_prompt(job_title, company, job_url, job_description)
        post_text = generate_with_gpt(prompt)
    else:
        print("\nPaste the LinkedIn-style post content. When you're done, press:")
        print(" - Ctrl+D (Mac/Linux) OR")
        print(" - Ctrl+Z then Enter (Windows)\n")
        post_text = sys.stdin.read().strip()

    return format_to_jsonl(job_title, company, job_url, job_description, post_text)

def save_to_jsonl(data, filename="data/linkedin_posts.jsonl"):
    with open(filename, "a", encoding="utf-8") as f:
        json.dump(data, f)
        f.write("\n")
    print(f"✅ Saved to {filename}")

if __name__ == "__main__":
    while True:
        mode = input("Do you want to auto-generate the LinkedIn post using GPT? (y/n): ")
        auto_generate = mode.lower() == 'y'
        data = collect_job_post(auto_generate=auto_generate)
        save_to_jsonl(data)
        more = input("\nDo you want to add another post? (y/n): ")
        if more.lower() != 'y':
            break
