def get_weight_range(age, gender):
    if gender.lower() == 'male':
        if 13 <= age <= 19:
            return 45, 69
        elif 19 < age <= 29:
            return 69, 84
        elif age >= 30:
            return 84, 90
    elif gender.lower() == 'female':
        if 13 <= age <= 19:
            return 45, 57
        elif 19 < age <= 29:
            return 57, 73
        elif age >= 30:
            return 73, 77
    return None

def categorize_feelings(feelings):
    positive_keywords = ['happy','Happy','Joyful','confident','Confident','Excited','exited','realxed','Relaxed','euphoria','Euphoria', 'joyful', 'positive', 'content','glad']
    depression_keywords = ['cry','crying','depressed','Depression','Depressed', 'depression','low','loneliness','Loneliness','loss of interest','not intersted in anything']
    stress_keywords = ['tired', 'stress', 'stressed','Stressed','Stress','worry','Worry','Worried','worried','strain','Tensed','tension','tensed','feeling pressured','uneasiness']
    anxiety_keywords = ['breakdown','broken down','broke down','anxious', 'angry','panic','Panic','uneasy','Uneasy','fearful','Fearful','nervousness','Nervousness','nervous','concern','Concerned','concern','Disturbed','disturbed']

    if any(keyword in feelings for keyword in positive_keywords):
        return 'positive'
    elif any(keyword in feelings for keyword in depression_keywords):
        return 'depression'
    elif any(keyword in feelings for keyword in stress_keywords):
        return 'stress'
    elif any(keyword in feelings for keyword in anxiety_keywords):
        return 'anxiety'
    else:
        return None  

def categorize_behavior(sentence):
    positive_keywords = ['kind', 'helpful', 'positive', 'friendly']
    negative_keywords = ['rude', 'unhelpful', 'negative', 'unfriendly']

    if any(keyword in sentence for keyword in positive_keywords):
        return 'positive'
    elif any(keyword in sentence for keyword in negative_keywords):
        return 'negative'
    else:
        return None

def analyze_food_habits(meals_per_day):
    if meals_per_day is not None and meals_per_day >= 3:
        return "Your meal habits seem to be proper. Well-balanced meals contribute to overall well-being."
    elif meals_per_day is not None:
        return "Consider having at least three meals a day for a more balanced and nutritious diet."
    else:
        return "Meal information not provided."

def analyze_sleep_duration(sleep_hours):
    if sleep_hours is not None:
        if 7 <= sleep_hours <= 9:
            return "Great! You're getting an optimal amount of sleep. Keep it up for overall well-being."
        elif 6 <= sleep_hours < 7:
            return "Your sleep duration is slightly below the recommended range. Aim for 7-9 hours for better mental health."
        elif 9 <= sleep_hours <= 10:
            return "Your sleep duration is slightly above the recommended range. Aim for 7-9 hours for better mental health."
        elif sleep_hours < 6:
            return "Your sleep duration is below the recommended range. Ensure you get 7-9 hours for better mental health."
        elif sleep_hours > 10:
            return "Your sleep duration is above the recommended range. Aim for 7-9 hours for better mental health."
    else:
        return "Sleep information not provided."

def analyze_symptoms(feelings_category, behavior_category, meals_per_day, sleep_hours):
    symptoms = []
    if behavior_category == 'negative':
        symptoms.append('Irritable behavior')
    if feelings_category == 'depression':
        symptoms.append('Low mood')
    if feelings_category == 'anxiety':
        symptoms.append('Feelings of unease or fear')
    if feelings_category == 'stress':
        symptoms.append('High stress levels')
    if meals_per_day is not None and meals_per_day < 3:
        symptoms.append('Poor eating habits')
    if sleep_hours is not None and (sleep_hours < 7 or sleep_hours > 9):
        symptoms.append('Irregular sleep patterns')

    return symptoms

def conclude_overall_feeling(symptoms):
    if len(symptoms) >= 3:
        return "Overall Feeling: You might be facing difficulties. Consider seeking support from friends, family, or professionals.", "Analysis Result: The symptoms suggest a combination of issues, possibly depression, anxiety, or stress. Seeking professional help is recommended."
    elif len(symptoms) == 2:
        return "Overall Feeling: You may be facing some challenges. Consider making positive changes in your habits.", "Analysis Result: The symptoms indicate some concerns in your habits. Focus on improving them for better well-being."
    elif len(symptoms) == 1:
        return "Overall Feeling: You seem to be doing well. Keep focusing on positive habits.", "Analysis Result: The symptoms are minimal, and overall, you're doing okay."
    else:
        return "Overall Feeling: You seem to be doing well. Keep focusing on positive habits.", "Analysis Result: Your habits are generally positive, and there are no major concerns."

def provide_suggestions(feelings_category, symptoms, sleep_hours):
    suggestions = []

    if feelings_category == 'depression':
       suggestions.extend([
    "1)Consult a mental health professional for personalized advice.",
    "2)If you need immediate support, call the NATIONAL SUCIDE PREVENTION LIFELINE: 1-800-273-TALK (1-800-273-8255),call ARPITHA SUCIDE PREVENTION HELPLINE- 080-23655557,VANDREVALA FOUNDATION- 9999 666 555,PARIVARTHAN-+91-7676602602.",
    "3)Consider MINDFULLNESS and MEDITATION for managing depressive symptoms.",
    "4)MOTIVATIONAL QUOTE: 'Believe you can and you're halfway there.'"
      ])

    elif feelings_category == 'anxiety':
        suggestions.extend([
            "1)Establish a consistent sleep schedule for better overall well-being.",
            "2)Engage in stress-reducing activities such as meditation or yoga.",
            "3)Consider seeking support from a mental health professional.",
            "4)Try this relaxing yoga exercise: [Yoga exercise details:'Uttanasana','Marjaryasana','Balasana','Bitilasana'].",
            "5)Ensure you maintain healthy food habits for improved mental well-being."
        ])
        if sleep_hours is not None and sleep_hours < 7:
            suggestions.append("Improve Sleep: Ensure you get enough sleep for better mental health.")
    elif feelings_category == 'stress':
        suggestions.extend([
            "1)Consider talking to a friend or family member about your feelings.",
            "2)Take a break and engage in activities you enjoy.",
            "3)Practice deep breathing exercises for relaxation.",
            "4)Listen to your favorite calming music."
            "5)Learn the “5 A's” to better manage stress, which includes avoiding, altering, adapting, accepting, and being active."
        ])

    if 'Irritable behavior' in symptoms:
        suggestions.append("Work on improving your behavior towards others. Practicing kindness can positively impact your mental well-being.")

    if symptoms:
        suggestions.append("Consider making positive changes in your habits to address the identified symptoms.")

    return suggestions

def main():
    print("Welcome to the Mental Health Checkup!")

    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ")
    weight_range = get_weight_range(age, gender)

    if weight_range is None:
        print("Invalid age or gender. Please ensure you provide accurate information.")
        return

    weight = int(input("Enter your weight in kg: "))

    if weight_range[0] <= weight <= weight_range[1]:
        print(f"Your weight is within the recommended range for your age and gender.")
    else:
        print(f"Your weight should be between {weight_range[0]}kg and {weight_range[1]}kg for your age and gender. Please maintain a healthy weight.")

    while True:
        behavior_sentence = input("Describe what are you feelings and what problems you are facing: ").lower()
        behavior_category = categorize_behavior(behavior_sentence)

        feelings = input("Describe your overall feelings: ").lower()
        feelings_category = categorize_feelings(feelings)

        meals_per_day = int(input("How many meals do you eat per day? "))
        sleep_hours = int(input("How many hours do you sleep per night? "))

        print("\n** Additional Analysis Results **")
        food_habits_result = analyze_food_habits(meals_per_day)
        print(food_habits_result)

        sleep_result = analyze_sleep_duration(sleep_hours)
        print(sleep_result)

        symptoms = analyze_symptoms(feelings_category, behavior_category, meals_per_day, sleep_hours)

        overall_feeling_result, analysis_result = conclude_overall_feeling(symptoms)
        if overall_feeling_result is not None and analysis_result is not None:
            print("\n** Overall Feeling and Analysis Result **")
            print(overall_feeling_result)
            print(analysis_result)

            print("\n** Suggestions **")
            suggestions = provide_suggestions(feelings_category, symptoms, sleep_hours)
            if suggestions:
                print("Here are some suggestions:")
                for suggestion in suggestions:
                    print(suggestion)

if __name__ == "__main__":
    main()