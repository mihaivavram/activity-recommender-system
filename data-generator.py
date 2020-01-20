import csv
import random

# User activity completion and review as a percentage e.g. 0.5 -> 50%
CHANCE_RATED = 0.5
HEADERS = ['user_id', 'activity_id', 'review']
NUM_USERS = 10
NUM_ACTIVITIES = 10


def generate_dummy_activity_data():
    '''Generates a csv file with user, action, and review data and the
           following columns: (user_id, activity_id, review)
    '''
    with open('./data/generated_activity_reviews.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            # Writing the header/title row
            csv_writer.writerow(HEADERS)

            # Generating dummy row data
            for user in range(0, NUM_USERS):
                for activity in range(0, NUM_ACTIVITIES):
                    has_rated = True if (
                        random.random() <= CHANCE_RATED) else False
                    review = None
                    if has_rated:
                        review = random.randint(0, 10)

                    csv_writer.writerow([user, activity, review])


def main():
    generate_dummy_activity_data()


if __name__ == '__main__':
    main()
