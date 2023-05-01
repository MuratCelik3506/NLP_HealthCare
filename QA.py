from transformers import pipeline

# qa_model = pipeline("question-answering")
# data = "A new study, published Online First in The Lancet , reports that major complications during early surgical abortions are reduced by nearly a third in comparison with placebo, if the cervix is prepared with misoprostol. Misoprostol is widely used for cervical preparation before surgical abortion (vacuum aspiration), given that the drug is effective, easy to use, cheap and widely available. However, there have been no studies, until now, that were sufficiently large to evaluate if misoprostol causes immediate or delayed serious complications from surgical abortion. In a multinational, randomized study, Eduardo Bergel from WHO in Geneva, Switzerland, and his team compared complications rates of vacuum aspirations in terms of incomplete abortion, cervical tear, pelvic inflammatory disease, uterine perforation, or other serious events. The study recruited 4,972 women who requested an abortion before the 12th week of pregnancy, from 14 centers in nine countries. 2,485 women were randomly assigned for administration with vaginal misoprostol, whilst 2,487 women received placebo 3 hours before aspiration. The results showed that the risk of experiencing one or more complications was almost a third lower for women in the misoprostol group than that of those who received placebo, whilst minor cervical tears and uterine perforations were also observed to be less frequent in the misoprostol group. They also found an almost three times increased risk of incomplete abortion in the placebo group compared with women in the misoprostol group. The researchers also noted that women in the misoprostol group more frequently experienced abdominal pain, vaginal bleeding, and nausea after being treated with misoprostol during the 3 hours before surgery, however, no differences were observed between both groups with regard to incidences of pelvic inflammatory disease or other serious adverse events. In a concluding statement the researchers state: “ Misoprostol reduced the overall incidence of complications, particularly incomplete abortions and unscheduled clinic visits and hospital admissions after abortion…Providers should be aware of the side-effects of the drug and inform women about these effects. ” According to a linked comment made by Allan Templeton from the University of Aberdeen in Scotland: “ The important issue…is the balance between effectiveness of the procedure and the side-effects of misoprostol, which will include abdominal cramps and vaginal bleeding in most women, although not to the extent of needing medical intervention before surgery. Surely routine pharmaceutical dilation of the cervix should be recommended as an integral part of surgical abortion in all women. ” Written by Petra Rattue"
# question = "What is the name of the drug that helps in abortion?"
# answer = qa_model(question = question, context = data)
# print(answer)

global qa_model

def initialize_model():
    global qa_model
    qa_model = pipeline("question-answering")

