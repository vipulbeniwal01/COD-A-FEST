from transformers import pipeline

def summarize(text, max_length=150, min_length=50):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    text = """ The prison authorities rejected Pathak’s request saying he misused the facility by making statements against the prison administration in violation of prison rules, which say the conversation between an inmate and visitor shall be limited to private and domestic matters.

Pathak moved the high court seeking to quash the decision of the Tihar authorities and direct them to permit him to meet Kejriwal. He claimed the statements he made after meeting Kejriwal were apolitical.

Justice Krishna rejected the contention, saying political statements have been made on Kejriwal’s behalf even as he has been unable to address the public or make such statements due to his imprisonment. She said as long as a person is confined to jail, he has to abide by the rules.

Senior advocate Rahul Mehra, who appeared for Pathak, argued that the term politics under Rule 587 cited for the rejection referred to the loose conversation about jail administration and not politics.

Justice Krishna said the argument did not hold water. “There is not an iota of doubt that the statements made by the petitioner were political, for and on behalf of Shri Arvind Kejriwal and were clearly violative of Rule 587...”

In its 15-page ruling, the court rejected Mehra’s contention that the restrictions were violative of the rights of citizens and their freedom of speech. It said the rule restricting the visitor’s rights is intended to maintain proper discipline. “The petitioner had made the statements for and on behalf of Shri Arvind Kejriwal and he was more like an agent or spokesperson and his statements cannot be held to have been made by him in the exercise of the free right to speech and expression or violative of reasonable restrictions imposed by DPR [Delhi Prison Rules]."""
    print(summarize(text))