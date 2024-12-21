import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.url = "https://merotutor.com/list/55/1/all-subjects-teachers-bachelors-degree-kathmandu"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def get_teacher_data(self):
        response = self.session.get(self.url)
        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        teacher_cards = soup.find_all('div', class_='teacher_outer_box')
        teachers = []

        for card in teacher_cards:
            name = card.find('div', class_='tutorFullName tutorRow').text.strip() if card.find('div', class_='tutorFullName tutorRow') else None
            age_gender = card.find('div', class_='tutorAgeGender tutorRow').text.strip() if card.find('div', class_='tutorAgeGender tutorRow') else None
            education = card.find('div', class_='tutorEducation tutorRow').text.strip() if card.find('div', class_='tutorEducation tutorRow') else None
            experience = card.find('div', class_='tutorTeachingExp tutorRow').text.strip() if card.find('div', class_='tutorTeachingExp tutorRow') else None
            qualification = education 
            profile_link = card.find('a', href=True)['href'] if card.find('a', href=True) else None

            subjects = "Not specified"
            location = "Not specified" 

            teacher = {
                'name': name,
                'age_gender': age_gender,
                'education': education,
                'experience': experience,
                'qualification': qualification,
                'subjects': subjects,
                'location': location,
                'profile_url': profile_link
            }
            teachers.append(teacher)

        return teachers
