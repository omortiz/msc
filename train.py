from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train(
        "chatterbot.corpus.english.greetings"
    )

    trainer = ListTrainer(bot)

    trainer.train([
        "Hi there!",
        "Hello",
    ])

    trainer.train([
        "Greetings!",
        "Hello",
    ])

    trainer.train([
        "Bye now",
        "Have a good day!"
    ])

    trainer.train([
        "Bye bye",
        "Have a good day"
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
        'This should help get you started: \n http://chatterbot.rtfd.org/en/latest/quickstart.html'
    ])


def trainSet2(bot):
    trainer = ListTrainer(bot)

    for pair in HRdataList:
        trainer.train(pair)

def trainSet3(bot):
    trainer = ListTrainer(bot)

    trainer.train([
        "Hi Rob!",
        "Greetings!"
    ])

    trainer.train([
        "Hello Rob!",
        "Greetings!"
    ])

    trainer.train([
        "Hi Rob!",
        "Hi there!"
    ])

    trainer.train([
        "Hello Rob!",
        "Hello there!"
    ])

    trainer.train([
        "What are you?",
        "I am a digital assistant"
    ])

    trainer.train([
        "Who are you?",
        "My name is Rob and I'm a digital assistant"
    ])

    trainer.train([
        "What is your name?",
        "My name is Rob."
    ])

    trainer.train([
        "Are you a robot?",
        "Not yet. For now, I am just a digital assistant"
    ])

    trainer.train([
        "Who made you?",
        "I was created by Team Team, a group of students from the University of California, Irvine."
    ])

    trainer.train([
        "Who created you?",
        "I was created by Team Team, a group of students from the University of California, Irvine."
    ])

    trainer.train([
        "Who developed you?",
        "I was created by Team Team, a group of students from the University of California, Irvine."
    ])

    trainer.train([
        "Why were you made?",
        "I was created as a senior project at the University of California, Irvine."
    ])

    trainer.train([
        "Why were you created?",
        "I was created as a senior project at the University of California, Irvine."
    ])

    trainer.train([
        "Why were you developed?",
        "I was created as a senior project at the University of California, Irvine."
    ])

    trainer.train([
        "What is your purpose?",
        "I can answer questions about MSC Software."
    ])

    trainer.train([
        "What can you do?",
        "I can answer questions about MSC Software."
    ])

    trainer.train([
        "Are you a person?",
        "No. I am a digital assistant."
    ])

    trainer.train([
        "Help!",
        "What can I help you with?",
        "I need to know some information.",
        "I can help with that!"
    ])

    trainer.train([
        "Who are you?",
        "My name is Rob and I'm a digital assistant",
        "What can you do?",
        "I can answer questions about MSC Software",
        "Are you a human?",
        "No. I am a digital assistant."

    ])

    trainer.train([
        "Hi there! How can I help you?",
        "I need to find some information about MSC Software.",
        "I can help with that!",
        "Great, thanks!",
        "What can I help you with?",
        "What city is MSC Software located in?",
        "MSC Software is located in the city of Newport Beach, CA.",
        "Okay, thanks.",
        "You're welcome!"
    ])

    trainer.train([
        "Hi, can I help you?",
        "Yes, I would like information about my 401K.",
        "Here is a link where you can find information about your 401K: \n https://www.irs.gov/retirement-plans/401k-plans"
        "Thanks Rob!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "I need to know who is the CEO of the company",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thanks Rob!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the current CEO of the company?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thanks Rob!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the CEO of the company?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the CEO of MSC Software?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is MSC Software's CEO?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is MSC Software's Chief Executive Officer?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the company's CEO?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the company's Chief Executive Officer?",
        "The current CEO of MSC Software is Paolo Guglielmini.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the company's Chief Financial Officer?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the CFO?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the Chief Financial Officer?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the current CFO?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is the current CFO of MSC Software?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is MSC Software'es CFO?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thanks Rob!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi there! How can I help you?",
        "Who is MSC Software'es current CFO?",
        "The current CFO of MSC Software is Kevin Rubin.",
        "Thanks Rob!",
        "You're welcome!"
    ])

    trainer.train([
        "Who is MSC Software'es Chief Financial Officer?",
        "The current CFO of MSC Software is Kevin Rubin."
    ])

    trainer.train([
        "Who is the company's Chief Financial Officer?",
        "The current CFO of MSC Software is Kevin Rubin."
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
        "Hi there! How can I help you?",
        "When was MSC founded?",
        "MSC Software was founded in 1963.",
        "Thank you!",
        "You're welcome!"
    ])

    trainer.train([
        "Hello! How can I help you?",
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
        "Where is MSC Software located?",
        "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
    ])

    trainer.train([
        "Where is MSC located?",
        "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
    ])

    trainer.train([
        "Where is the company located?",
        "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
    ])

    trainer.train([
        "Hi! How can I help you?",
        "What's the phone number of MSC Software?",
        "The phone number for MSC Software (714) 540-8900.",
        "Okay, thanks!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi! How can I help you?",
        "What's the company's phone number?",
        "The phone number for MSC Software (714) 540-8900.",
        "Okay, thanks!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi! How can I help you?",
        "What's MSC Software's phone number?",
        "The phone number for MSC Software (714) 540-8900.",
        "Okay, thanks!",
        "You're welcome!"
    ])

    trainer.train([
        "Hi! How can I help you?",
        "What's MSC Software?",
        "MSC Software Corporation is an American software company based in Newport Beach, California, that specializes in simulation software.",
        "Okay, thanks!",
        "You're welcome!"
    ])

    trainer.train([
        "What does MSC Software do?",
        "MSC Software Corporation is an American software company based in Newport Beach, California, that specializes in simulation software."
    ])

    trainer.train([
        "What does the company do?",
        "MSC Software Corporation is an American software company based in Newport Beach, California, that specializes in simulation software."
    ])

    trainer.train([
        "What does MSC Software produce?",
        "MSC Software Corporation is an American software company based in Newport Beach, California, that specializes in simulation software."
    ])

    trainer.train([
        "What does MSC Software make?",
        "MSC Software Corporation is an American software company based in Newport Beach, California, that specializes in simulation software."
    ])

    trainer.train([
        "What are some products made by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some products developed by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What is some software made by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What is some software developed by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What is some software made by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What is some software developed by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some products developed by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some products made by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What software is made by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What software is developed by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What software is produced by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What software is made by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What software is developed by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What things are produced by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What things are made by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What things are developed by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things developed by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things made by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things produced by MSC Software?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things developed by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things made by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are some things produced by the company?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What does MSC Software work on?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What does company work on?",
        "MSC Software has created the following products: MSC Apex, Actran, Adams, Digimat, Dytran, Easy5, Marc, MaterialCenter, MSC Fatigue, MSC Nastran, Patran, SimDesigner, SimManager, SimXpert, and Sinda"
    ])

    trainer.train([
        "What are my employee benefits?",
        "Your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "What are my work benefits?",
        "Your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "What are my benefits?",
        "Your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "What benefits do I have?",
        "Your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "I need to see a doctor. Does my insurance cover me?",
        "Yes, your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "I need to see a doctor. Does my employee insurance cover me?",
        "Yes, your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "I need to see a doctor.",
        "Your employee benefits include Health, Dental, and Vision. Here's a link for more information: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "Hi Rob!",
        "Hello there!",
        "I sprained my ankle",
        "Do you need to see a doctor?",
        "Yes. I need to see a doctor.",
        "Your employee benefits include Health, Dental, and Vision.",
        "Where can I find more information about my benefits?",
        "Here's a link: https://www.mscsoftware.com/us-benefits"
    ])

    trainer.train([
        "Hey Rob!",
        "Hello there!",
        "Do you need to see a doctor?",
        "Yes.",
        "Your employee benefits include Health, Dental, and Vision.",
        "Where can I find more information about my benefits?",
        "Here's a link: https://www.mscsoftware.com/us-benefits"
        ])

