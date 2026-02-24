from transformers import pipeline
# load hugging face text generation model
generator=pipeline
(
"text-generation",
model="gpt2-medium"
)
#notes generator function

def f1(topic):
    prompt=f"write simple beginner-friendly notes in bulletpoints{topic}"
    result==generator
    (
        prompt,
        max_length=150,
        temperature=0.7
         #control cretaion
        repetition_penalty=1.5
        do_sample=True
        num_return_sequences=1 
    )
    return result[0]["generated_text"]
topic =input("enter the topic name")
a=f1(topic)
print(a)
