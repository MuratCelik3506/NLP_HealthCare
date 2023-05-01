import os
from transformers import pipeline


# if os.path.exists("summary"):
#     pass
# else:
#     os.mkdir("summary")
#
#
# summarize = pipeline("summarization")
#
# for file_name in os.listdir("articles")[1:4]:
#     print(file_name)
#     with open(f'articles/{file_name}', 'r', encoding="utf8") as file:
#         data = file.read().replace('\n', '')
#     try:
#         summary_text = summarize(data)
#         sum_text = summary_text[0]["summary_text"]
#     except:
#         sentences = list(data.split("."))
#         print(len(sentences))
#         first_paragraph = sentences[:len(sentences)//2]
#         first_paragraph = ".".join(first_paragraph)
#         second_paragraph = sentences[len(sentences)//2:]
#         second_paragraph = ".".join(second_paragraph)
#         try :
#             summary_text_1 = summarize(first_paragraph)
#             summary_text_2 = summarize(second_paragraph)
#             sum_text = summary_text_1[0]["summary_text"] + summary_text_2[0]["summary_text"]
#         except:
#             print(f"{file_name} give error")
#
#     print(sum_text)
#
summarize = ""
before_run = True




def summarize_text(text):
    global summarize
    global before_run
    if before_run:
        summarize = pipeline("summarization")
        before_run = False
    #print(before_run)
    try:
        summary_text = summarize(text)
        sum_text = summary_text[0]["summary_text"]
    except:
        sentences = list(text.split("."))
        try:
            first_paragraph = sentences[:len(sentences) // 2]
            first_paragraph = ".".join(first_paragraph)
            second_paragraph = sentences[len(sentences) // 2:]
            second_paragraph = ".".join(second_paragraph)

            summary_text_1 = summarize(first_paragraph)
            summary_text_2 = summarize(second_paragraph)
            sum_text = summary_text_1[0]["summary_text"] + summary_text_2[0]["summary_text"]
        except:
            try:
                first_paragraph = sentences[:len(sentences) // 3]
                first_paragraph = ".".join(first_paragraph)
                second_paragraph = sentences[len(sentences) // 3:len(sentences) // 3 * 2]
                second_paragraph = ".".join(second_paragraph)
                third_paragraph = sentences[len(sentences) // 3 * 2:]
                third_paragraph = ".".join(third_paragraph)

                summary_text_1 = summarize(first_paragraph)
                summary_text_2 = summarize(second_paragraph)
                summary_text_3 = summarize(third_paragraph)
                sum_text = summary_text_1[0]["summary_text"] + summary_text_2[0]["summary_text"] + summary_text_3[0]["summary_text"]
            except:
                return f"Text give error"
    return sum_text

