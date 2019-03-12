
<<<<<<< HEAD
from chatterbot.trainers import ListTrainer
from multiprocessing.connection import Listener

HRdataList = [["How do I find out about job openings?",
"Visit our career site. Before applying we ask that you carefully read the job description to ensure you fulfill the requirements and are interested in the position."],
["How long are jobs posted?",
"Job openings are posted for a minimum of five business days or longer, depending on the position."],
["How do I apply for a job?",
"You must apply online to be considered. Click the 'Apply for this job'  button located next to the job listing."],
["How long will my application be kept online?",
"Your application material will be retained for at least one year. "],
["How can I update an application or cover letter that I previously turned in?",
"Job specific questions cannot be changed once submitted."],
["How can I update an application or cover letter that I previously turned in?",
"Profile level questions can be changed at any time by using the link on the candidate profile."],
["What is Employee Child Care Assistance Program? (ECCAP)",
"ECCAP is a program offered to assist faculty and staff to meet the cost of childcare."],
["My doctor does not accept Medicare. Will I still receive reimbursement from the Medicare Plan?",
"If your doctor does not accept Medicare, the plan will reimburse you as if Medicare paid its portion of the expense. "],
["What is the University's short term Disability Policy?",
"If your none work-related illness or injury is serious and requires you to be absent for 8 or more consecutive calendar days, you can apply for short term disability leave."],
["What will I be paid?",
"Full base pay is up to 12 weeks and 75% of base salary for an additional 14 weeks."],
["What should I do if I do not come to work?",
"You should notify your supervisor as soon as possible if you cannot or choose not to report to work at all. The entire day is charged to leave without pay or, if your supervisor approves, paid time off."]]

def trainSet1(bot):
    trainer = ListTrainer(bot)

=======

from chatterbot.trainers import ListTrainer
from multiprocessing.connection import Listener

HRdataList = [["How do I find out about job openings?",
"Visit our career site. Before applying we ask that you carefully read the job description to ensure you fulfill the requirements and are interested in the position."],
["How long are jobs posted?",
"Job openings are posted for a minimum of five business days or longer, depending on the position."],
["How do I apply for a job?",
"You must apply online to be considered. Click the 'Apply for this job'  button located next to the job listing."],
["How long will my application be kept online?",
"Your application material will be retained for at least one year. "],
["How can I update an application or cover letter that I previously turned in?",
"Job specific questions cannot be changed once submitted."],
["How can I update an application or cover letter that I previously turned in?",
"Profile level questions can be changed at any time by using the link on the candidate profile."],
["What is Employee Child Care Assistance Program? (ECCAP)",
"ECCAP is a program offered to assist faculty and staff to meet the cost of childcare."],
["My doctor does not accept Medicare. Will I still receive reimbursement from the Medicare Plan?",
"If your doctor does not accept Medicare, the plan will reimburse you as if Medicare paid its portion of the expense. "],
["What is the University's short term Disability Policy?",
"If your none work-related illness or injury is serious and requires you to be absent for 8 or more consecutive calendar days, you can apply for short term disability leave."],
["What will I be paid?",
"Full base pay is up to 12 weeks and 75% of base salary for an additional 14 weeks."],
["What should I do if I do not come to work?",
"You should notify your supervisor as soon as possible if you cannot or choose not to report to work at all. The entire day is charged to leave without pay or, if your supervisor approves, paid time off."]]

def trainSet1(bot):
    trainer = ListTrainer(bot)

>>>>>>> 035d2668b774adc7aa50e06c9c991a0fc26b2cf8
    trainer.train([
    "Hi there!",
    "Hello",
    ])

    trainer.train([
    "Greetings!",
    "Hello",
    ])

    trainer.train([
    "Are you a human?",
    "I'm a digital assistant.",
    ])

    trainer.train([
    "What are you",
    "I'm a digital assistant.",
    ])

    trainer.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
    ])

def trainSet2(bot):
    trainer = ListTrainer(bot)
    
    for pair in HRdataList:
        trainer.train(pair)
        
def trainSet3(bot):
    trainer = ListTrainer(bot)
    
    trainer.train([
            "Hi, can I help you?",
            "Yes, I would like information about my 401K?",
            "Here is a link where you can find information about your 401K: https://www.irs.gov/retirement-plans/401k-plans"
            "Thanks Rob!",
            "You're welcome!"
        ])

    trainer.train([
            "Hi there! How can I help you?",
            "I need to know who is the CEO of the company",
            "The current CEO of MSC Software is Paolo Guglielmini."
            "Thanks Rob!",
            "You're welcome!"
        ])

    trainer.train([
            "Hi there! How can I help you?",
            "Who is the current CFO?",
            "The current CFO of MSC Software is Kevin Rubin."
            "Thanks Rob!",
            "You're welcome!"
        ])

    trainer.train([
            "How can I help you?",
            "When was the company founded?",
            "MSC Software was founded in 1963.",
            "Thanks Rob!",
            "You're welcome!"
        ])

    trainer.train([
            "Hi there! How can I help you?",
            "When was MSC Software founded?",
            "MSC Software was founded in 1963.",
            "Thanks Rob!",
            "You're welcome!"
        ])

    trainer.train([
            "Hello! How can I help you?"
            "What's the address of MSC Software?",
            "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
            "Okay thanks!",
            "Your're welcome! Is there anything else I can do for you?",
            "No, thanks!"
        ])

    trainer.train([
            "Hi! How can I help you?",
            "What's the company's address?",
            "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
            "Do you need anything else?",
            "No, thank you!",
            "Have a good day!",
            "Thanks, you too!"
        ])

    trainer.train([
            "Hi! How can I help you?",
            "What's the phone number of MSC Software?",
            "The phone number for MSC Software (714) 540-8900.",

        ])

    trainer.train([
            "Hi! How can I help you?",
            "What's MSC Software's phone number?",
            "The phone number for MSC Software (714) 540-8900.",

        ])
<<<<<<< HEAD
=======

>>>>>>> 035d2668b774adc7aa50e06c9c991a0fc26b2cf8
