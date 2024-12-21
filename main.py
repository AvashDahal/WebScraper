from scraper import Scraper
from dbOperation import DatabaseOperations


def main():
    scraper = Scraper()
    db = DatabaseOperations()
    
    # Create database table
    db.create_table()
    
    # Get teacher data
    print("Starting to scrape teacher data...")
    teachers = scraper.get_teacher_data()
    
    # Store teachers in the database
    successful_inserts = 0
    for teacher in teachers:
        if db.insert_teacher(teacher):
            successful_inserts += 1
            print(f"Stored teacher: {teacher['name']}")
    
    print("\nScraping completed!")
    print(f"Total teachers found: {len(teachers)}")
    print(f"New teachers added: {successful_inserts}")


if __name__ == "__main__":
    main()
