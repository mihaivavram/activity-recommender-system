import argparse
import numpy as np
import pandas as pd


def find_correlation(first_activity, second_activity):
    '''Finds the Pearson R correlation between two activities

    Parameters
    ----------
    first_activity : int
        The activity id of the first activity to compare
    second_activity : int
        The activity id of the second activity to compare

    Returns
    -------
    corr : float
        Pearson correlation
    '''
    sum1 = first_activity - first_activity.mean()
    sum2 = second_activity - second_activity.mean()
    corr = np.sum(sum1 * sum2) / np.sqrt(np.sum(sum1 ** 2) * np.sum(sum2 ** 2))
    return corr


def find_recommendations(queried_activity, user_activity_matrix, num_recs):
    '''Returns a sorted list of top activity recommendations

    Parameters
    ----------
    queried_activity : int
        The id of the activity we want to find similar top recommendations for
    user_activity_matrix : Pandas DataFrame
        In the x-axis index we have the activity id, and the y-axis index,
        we have the user id
    num_recs : int
        Number of top recommendations to return

    Returns
    -------
    top_recommendations : list of tuples
        A sorted list of top activity recommendations (ordered by higher
        recommendation likelihood)
        e.g. [(id1, likelyhood1), (id2, likelyhood2), ...]
    '''
    top_recommended_activities = []

    for activity in user_activity_matrix.columns:
        if queried_activity == activity:
            continue
        else:
            correlation = find_correlation(
                user_activity_matrix[queried_activity],
                user_activity_matrix[activity]
            )
            if not np.isnan(correlation):
                top_recommended_activities.append((activity, correlation))

    top_recommendations = sorted(top_recommended_activities,
                                 key=lambda x: x[1])

    top_recommendations.reverse()
    return top_recommendations[0: num_recs]


def main():
    parser = argparse.ArgumentParser(
        description='Program with arguments to find activity recommendations'
    )

    parser.add_argument('--actid', action='store',
                        dest='activity_id', type=int)
    parser.add_argument('--topnrec', action='store',
                        dest='top_n_recommendations', type=int)

    args = parser.parse_args()

    if not args.activity_id:
        raise argparse.ArgumentTypeError(
            'Please provide the activity id with --actid <id> option'
        )

    reviews = pd.read_csv('./data/generated_activity_reviews.csv')
    user_activity_matrix = reviews.pivot_table(index=['user_id'],
                                               columns=['activity_id'],
                                               values='review')

    print('USER ACTIVITY REVIEW MATRIX: \n', user_activity_matrix)

    top_recommendations = find_recommendations(
        args.activity_id, user_activity_matrix, args.top_n_recommendations
    )

    print('TOP RECOMMENDATIONS in the format of (activity id, likelyhood): \n',
          top_recommendations)


if __name__ == '__main__':
    main()
