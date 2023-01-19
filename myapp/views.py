from django.shortcuts import render
import openai

# Create your views here.
openai.api_key = "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"

def generate_code(request):
    if request.method == "POST":
        natural_language = request.POST.get("natural_language")
        prompt = (f"Write a Python function that {natural_language}")
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        code = completions.choices[0].text
        return render(request, "code.html", {"code": code})
    else:
        return render(request, "index.html")